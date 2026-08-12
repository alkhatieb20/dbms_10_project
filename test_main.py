import pytest
from fastapi.testclient import TestClient
from main import app, EXPECTED_API_KEY


client = TestClient(app)


VALID_HEADERS = {"x-api-key": EXPECTED_API_KEY}
INVALID_HEADERS = {"x-api-key": "wrong-password-123"}

def test_unauthorized_access_rejected():
   
    payload = {
        "topic_id": 1,
        "question_text": "What is Linux?",
        "default_points": 10,
        "difficulty": "Easy"
    }
    
    
    response_no_key = client.post("/questions", json=payload)
    assert response_no_key.status_code == 422  
    
    
    response_wrong_key = client.post("/questions", json=payload, headers=INVALID_HEADERS)
    assert response_wrong_key.status_code == 401  

def test_read_courses():
  
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_business_rule_exam_points_aggregation():
    
    
    
    response = client.get("/exams/1/details")
    assert response.status_code == 200
    
    data = response.json()
    
    
    assert len(data["questions"]) >= 3
    
    
    actual_sum = sum(q["assigned_points"] for q in data["questions"])
    
    
    assert data["calculated_total_points"] == actual_sum
    assert data["calculated_total_points"] == 30