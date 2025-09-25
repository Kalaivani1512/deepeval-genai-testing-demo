# deepeval-genai-testing-demo
My first deepeval testing project in GitHub

This repository demonstrates **AI/ML testing** using **DeepEval**, a Python framework for evaluating generative AI models. The project showcases automated testing of **LLM outputs** with metrics like relevancy and faithfulness.

---

## **Table of Contents**
- [Overview](#overview)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Setup](#setup)  
- [Usage](#usage)  
- [Test Cases](#test-cases)  
- [Contributing](#contributing)  
- [License](#license)  

---

## **Overview**
DeepEval allows testers to validate the performance of **Generative AI models** by providing:

- Metric-based evaluation (Answer Relevancy, Faithfulness, Hallucination, Summarization, etc.)  
- Automated scoring of model outputs  
- Integration with pytest for **unit-test style testing**  
- Support for both OpenAI GPT models and local LLMs  

This demo project simulates testing **AI-generated answers** for different inputs using **mocked metrics**.

---

## **Technologies Used**
- Python 3.13  
- [DeepEval](https://pypi.org/project/deepeval/)  
- Pytest  
- unittest.mock (for offline testing without API calls)  

---

## **Installation**
1. Clone the repository:
```bash
git clone https://github.com/yourusername/deepeval-genai-testing-demo.git
cd deepeval-genai-testing-demo

2. Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

3. Install dependencies:
pip install -r requirements.txt

**Setup**
Optional: OpenAI API Key

If you want to run real metric evaluations using OpenAI GPT:

Get an API key from OpenAI

Set it as an environment variable:
1. Windows (PowerShell):
$env:OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"

2. Linux/Mac:
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"

**Usage**
Run all tests with pytest:
pytest test_genai.py -v

Sample mocked test output:
test_genai.py::test_answer_relevancy PASSED
test_genai.py::test_faithfulness PASSED

**Test Cases**

This demo includes:

1. Answer Relevancy — Checks if AI output matches expected answer
2. Faithfulness — Checks if AI output is factually correct
3. Mocked GenAI model outputs to allow offline testing without API calls

**Contributing**

1. Fork the repository
2. Create a feature branch (git checkout -b feature-name)
3. Commit your changes (git commit -m "Add feature")
4. Push to branch (git push origin feature-name)
5. Create a Pull Request

**License**

This project is licensed under the MIT License.

**Contact**

For any queries, reach out to: Kalaivani Anbumani
Email: kalaianbumani@gmail.com

