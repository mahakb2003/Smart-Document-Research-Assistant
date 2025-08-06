from backend.gemini_utils import gemini_answer

def answer_question(text, question):
    prompt = f"Answer this question based on the document:\n\n{text}\n\nQuestion: {question}"
    return gemini_answer(prompt)

def generate_questions(text):
    prompt = f"Generate 3 logical, understanding-based questions from this document:\n\n{text}"
    return gemini_answer(prompt).split("\n")

def evaluate_answers(questions, answers, text):
    evaluations = []
    for q, a in zip(questions, answers):
        prompt = f"Evaluate the following answer based on the document:\n\nQuestion: {q}\nAnswer: {a}\n\nDocument: {text}"
        evaluations.append(gemini_answer(prompt))
    return evaluations
