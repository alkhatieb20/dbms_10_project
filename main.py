import os
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI()

DB_URL = os.environ.get("DATABASE_URL")
EXPECTED_API_KEY = os.environ.get("API_KEY", "my-secret-x-api-key-123")

def get_db_connection():
    return psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)

def require_api_key(x_api_key: str = Header(...)):
    if x_api_key != EXPECTED_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

class QuestionCreate(BaseModel):
    topic_id: int
    question_text: str
    latex_content: str = ""
    default_points: int
    difficulty: str

@app.get("/courses")
def get_courses():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses;")
    courses = cursor.fetchall()
    
    for course in courses:
        cursor.execute("SELECT * FROM topics WHERE course_id = %s;", (course['course_id'],))
        course['topics'] = cursor.fetchall()
        
    cursor.close()
    conn.close()
    return courses

@app.get("/exams/{exam_id}/details")
def get_exam_details(exam_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    
    query = """
        SELECT e.exam_id, e.exam_title, e.exam_date,
               COALESCE(SUM(eq.assigned_points), 0) AS calculated_total_points
        FROM exams e
        LEFT JOIN exam_questions eq ON e.exam_id = eq.exam_id
        WHERE e.exam_id = %s
        GROUP BY e.exam_id, e.exam_title, e.exam_date;
    """
    cursor.execute(query, (exam_id,))
    exam = cursor.fetchone()
    
    if not exam:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Exam not found")
        
    
    q_query = """
        SELECT q.question_id, q.question_text, eq.sequence_order, eq.assigned_points 
        FROM questions q
        JOIN exam_questions eq ON q.question_id = eq.question_id
        WHERE eq.exam_id = %s
        ORDER BY eq.sequence_order;
    """
    cursor.execute(q_query, (exam_id,))
    exam['questions'] = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return exam

@app.post("/questions", dependencies=[Depends(require_api_key)])
def create_question(question: QuestionCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO questions (topic_id, question_text, latex_content, default_points, difficulty)
            VALUES (%s, %s, %s, %s, %s) RETURNING question_id;
            """,
            (question.topic_id, question.question_text, question.latex_content, question.default_points, question.difficulty)
        )
        conn.commit()
        return {"message": "Success"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()