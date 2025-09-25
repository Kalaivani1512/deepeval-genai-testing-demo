def generate_answer(question: str) -> str:
    """
    A simple mock function to simulate a GenAI model.
    In real life, this could call OpenAI, Hugging Face, or any LLM API.
    """
    if "AI" in question:
        return "Artificial Intelligence is the simulation of human intelligence in machines."
    elif "ML" in question:
        return "Machine Learning is a subset of AI that focuses on learning patterns from data."
    else:
        return "I'm not sure about that."
