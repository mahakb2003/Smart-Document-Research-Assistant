import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def gemini_answer(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_challenge_questions(text):
    prompt = f"Generate 5 comprehension-style questions from this document:\n\n{text}"
    response = gemini_answer(prompt)
    return response.split("\n")

def evaluate_user_answer(text, question, user_answer):
    prompt = (
        f"You are an evaluator. Here is a document excerpt:\n{text[:1000]}...\n\n"
        f"Question: {question}\n"
        f"User Answer: {user_answer}\n"
        f"Evaluate this answer fairly. Provide reasoning in 2-4 lines."
    )
    return gemini_answer(prompt)







