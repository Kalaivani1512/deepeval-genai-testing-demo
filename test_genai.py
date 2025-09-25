# test_genai.py
import pytest
from unittest.mock import MagicMock

# Mock DeepEval metrics classes
class AnswerRelevancyMetric:
    def __init__(self):
        pass

    def measure(self, actual_output, expected_output):
        # Simulate metric evaluation
        return {"score": 1.0, "success": True}

class FaithfulnessMetric:
    def __init__(self):
        pass

    def measure(self, actual_output, expected_output):
        return {"score": 1.0, "success": True}

# Mock function to simulate your GenAI app
def generate_answer(prompt: str) -> str:
    if "capital of France" in prompt:
        return "The capital of France is Paris."
    elif "AI" in prompt:
        return "Artificial Intelligence is the simulation of human intelligence in machines."
    return "I don't know."

# Test using mocked AnswerRelevancyMetric
def test_answer_relevancy():
    metric = AnswerRelevancyMetric()
    input_q = "What is the capital of France?"
    actual_output = generate_answer(input_q)
    expected_output = "The capital of France is Paris."

    result = metric.measure(actual_output, expected_output)
    assert result["success"] is True
    assert result["score"] == 1.0

# Test using mocked FaithfulnessMetric
def test_faithfulness():
    metric = FaithfulnessMetric()
    input_q = "What is AI?"
    actual_output = generate_answer(input_q)
    expected_output = "Artificial Intelligence is the simulation of human intelligence in machines."

    result = metric.measure(actual_output, expected_output)
    assert result["success"] is True
    assert result["score"] == 1.0
