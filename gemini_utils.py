#backend gemini util
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")  # or use gemini-1.5-pro

# -------- Function 1: Basic Answering --------
def gemini_answer(prompt):
    response = model.generate_content(prompt)
    return response.text

# -------- Function 2: Generate Challenge Questions --------
def generate_challenge_questions(text):
    prompt = f"""
You are a smart tutor. Based on the following text, generate 3 logic-based or comprehension questions like:

Q1. What is the main idea of...  
Q2. Explain two benefits of...  
Q3. What challenges are associated with...

Document:
{text}
"""
    response = model.generate_content(prompt)

    # Clean and extract only properly formatted questions
    raw_lines = response.text.strip().split('\n')
    questions = []
    for line in raw_lines:
        line = line.strip()
        if line.startswith("Q1.") or line.startswith("Q2.") or line.startswith("Q3."):
            questions.append(line)

    return questions


# -------- Function 3: Evaluate User's Answer --------
def evaluate_user_answer(document_text, question, user_answer):
    prompt = f"""You are an expert evaluator. Based on the document below, evaluate the user's answer to the question.

DOCUMENT:
{document_text}

QUESTION:
{question}

USER'S ANSWER:
{user_answer}

Respond with clear, helpful feedback in under 5 lines. Include justification from the document if possible."""
    
    response = model.generate_content(prompt)
    return response.text.strip()




