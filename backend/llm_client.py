from typing import Dict, Any, List
import time

class LLMClient:
    def __init__(self):
        self.model_name = "mock-llm-model"

    def predict(self, patient_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Mock prediction function that returns a simulated LLM response
        """
        # Simulate processing time
        time.sleep(0.5)
        
        # Mock response
        return {
            "prediction": 0.85,
            "confidence": 0.92,
            "explanation": "Based on the provided data, there is a high probability of CKD. Key risk factors include high blood pressure, diabetes, and age.",
            "risk_factors": ["high blood pressure", "diabetes", "age"]
        }