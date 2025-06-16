from typing import List, Dict, Any

def get_test_matrix() -> List[Dict[str, Any]]:
    """Get the test matrix for LLM evaluation"""
    return [
        # Test Case 1: High Risk Patient
        {
            "id": "high_risk_1",
            "prediction": {
                "prediction": 0.85,
                "confidence": 0.92,
                "explanation": "Based on the provided data, there is a high risk of CKD. Key risk factors include high blood pressure, diabetes, and age.",
                "risk_factors": ["high blood pressure", "diabetes", "age"],
                "response_time": 0.5
            },
            "ground_truth": {
                "prediction": 0.82,
                "risk_factors": ["high blood pressure", "diabetes", "age"]
            }
        },
        
        # Test Case 2: Low Risk Patient
        {
            "id": "low_risk_1",
            "prediction": {
                "prediction": 0.15,
                "confidence": 0.88,
                "explanation": "Based on the provided data, there is a low risk of CKD. The patient shows normal values for key indicators.",
                "risk_factors": ["normal blood pressure"],
                "response_time": 0.4
            },
            "ground_truth": {
                "prediction": 0.18,
                "risk_factors": ["normal blood pressure"]
            }
        },
        
        # Test Case 3: Edge Case - Very High Risk
        {
            "id": "edge_high_risk",
            "prediction": {
                "prediction": 0.98,
                "confidence": 0.95,
                "explanation": "Based on the provided data, there is an extremely high risk of CKD. Multiple severe risk factors are present.",
                "risk_factors": ["severe hypertension", "advanced diabetes", "kidney damage"],
                "response_time": 0.6
            },
            "ground_truth": {
                "prediction": 0.95,
                "risk_factors": ["severe hypertension", "advanced diabetes", "kidney damage"]
            }
        },
        
        # Test Case 4: Edge Case - Very Low Risk
        {
            "id": "edge_low_risk",
            "prediction": {
                "prediction": 0.02,
                "confidence": 0.90,
                "explanation": "Based on the provided data, there is an extremely low risk of CKD. All indicators are within normal ranges.",
                "risk_factors": ["normal kidney function"],
                "response_time": 0.3
            },
            "ground_truth": {
                "prediction": 0.05,
                "risk_factors": ["normal kidney function"]
            }
        },
        
        # Test Case 5: Missing Data
        {
            "id": "missing_data",
            "prediction": {
                "prediction": 0.50,
                "confidence": 0.60,
                "explanation": "Based on the limited data provided, there is an uncertain risk of CKD. More information is needed for accurate assessment.",
                "risk_factors": ["insufficient data"],
                "response_time": 0.4
            },
            "ground_truth": {
                "prediction": 0.45,
                "risk_factors": ["insufficient data"]
            }
        },
        
        # Test Case 6: Complex Case
        {
            "id": "complex_case",
            "prediction": {
                "prediction": 0.75,
                "confidence": 0.85,
                "explanation": "Based on the provided data, there is a moderate to high risk of CKD. Multiple factors contribute to this assessment.",
                "risk_factors": ["hypertension", "mild diabetes", "age", "family history"],
                "response_time": 0.7
            },
            "ground_truth": {
                "prediction": 0.72,
                "risk_factors": ["hypertension", "mild diabetes", "age", "family history"]
            }
        }
    ] 