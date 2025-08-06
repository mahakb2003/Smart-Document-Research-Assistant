from backend.gemini_utils import gemini_answer

def summarize_text(text):
    prompt = f"Summarize this document in 150 words or less:\n\n{text}"
    summary = gemini_answer(prompt)
    return summary.strip()








