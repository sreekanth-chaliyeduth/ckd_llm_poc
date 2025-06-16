import pytest

def test_llm_prediction_accuracy(mock_llm_client):
    """Test LLM prediction accuracy"""
    response = mock_llm_client.predict({"age": 65})
    
    # Test prediction format
    assert isinstance(response["prediction"], float)
    assert 0 <= response["prediction"] <= 1
    assert isinstance(response["confidence"], float)
    assert 0 <= response["confidence"] <= 1

def test_llm_response_time(mock_llm_client):
    """Test LLM response time"""
    import time
    start_time = time.time()
    mock_llm_client.predict({"age": 65})
    end_time = time.time()
    
    # Response should be fast (under 2 seconds)
    assert end_time - start_time < 2

def test_llm_error_handling(mock_llm_client):
    """Test LLM error handling"""
    # Test with invalid data
    mock_llm_client.predict.side_effect = Exception("Invalid data format")
    
    with pytest.raises(Exception):
        mock_llm_client.predict({"invalid": "data"})

def test_llm_explanation_quality(mock_llm_client):
    """Test the quality of LLM explanations"""
    response = mock_llm_client.predict({"age": 65})
    
    explanation = response["explanation"]
    
    # Check explanation length
    assert len(explanation) >= 50  # Explanation should be detailed
    
    # Check explanation content
    assert "risk" in explanation.lower()
    assert "factors" in explanation.lower() 