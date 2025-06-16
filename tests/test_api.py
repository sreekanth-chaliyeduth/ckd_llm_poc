import pytest
from fastapi.testclient import TestClient

def valid_patient_data():
    return {
        "age": 65,
        "blood_pressure": 140,
        "specific_gravity": 1.02,
        "albumin": 1,
        "sugar": 0,
        "red_blood_cells": "normal",
        "pus_cell": "normal",
        "pus_cell_clumps": "notpresent",
        "bacteria": "notpresent",
        "blood_glucose_random": 117,
        "blood_urea": 56,
        "serum_creatinine": 3.8,
        "sodium": 111,
        "potassium": 2.5,
        "hemoglobin": 11.2,
        "packed_cell_volume": 32,
        "white_blood_cell_count": 6700,
        "red_blood_cell_count": 3.9,
        "hypertension": "yes",
        "diabetes_mellitus": "yes",
        "coronary_artery_disease": "no",
        "appetite": "good",
        "pedal_edema": "yes",
        "anemia": "yes"
    }

def test_health_check(test_client):
    """Test the health check endpoint"""
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_endpoint(test_client):
    """Test the prediction endpoint with sample data"""
    payload = {"data": valid_patient_data()}
    response = test_client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_endpoint_invalid_data(test_client):
    """Test the prediction endpoint with invalid data"""
    payload = {"data": {"invalid": "data"}}
    response = test_client.post("/predict", json=payload)
    assert response.status_code == 200

def test_predict_endpoint_missing_data(test_client):
    """Test the prediction endpoint with missing data key"""
    response = test_client.post("/predict", json={})
    assert response.status_code == 422 