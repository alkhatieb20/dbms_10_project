import requests


BASE_URL = "http://localhost:8000"
HEADERS = {}

def get_courses() -> list[dict]:
    
    r = requests.get(f"{BASE_URL}/courses", headers=HEADERS, timeout=5)
    r.raise_for_status() 
    return r.json()

def create_question(topic_id: int, question_text: str, latex_content: str, default_points: int, difficulty: str) -> dict:
    
    payload = {
        "topic_id": topic_id,
        "question_text": question_text,
        "latex_content": latex_content,
        "default_points": default_points,
        "difficulty": difficulty
    }
    r = requests.post(f"{BASE_URL}/questions", json=payload, headers=HEADERS, timeout=5)
    r.raise_for_status()
    return r.json()

def get_exam_details(exam_id: int) -> dict:
    
    r = requests.get(f"{BASE_URL}/exams/{exam_id}/details", headers=HEADERS, timeout=5)
    r.raise_for_status()
    return r.json()