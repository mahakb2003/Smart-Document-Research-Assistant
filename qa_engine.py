
# backend/qa_engine.py
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(question, context):
    # Create a custom prompt to guide the model
    prompt = f"""
    You are a research assistant. Based only on the document content below, answer the question as clearly and completely as possible. Include only what is supported by the document.

    Document:
    {context}

    Question: {question}
    Answer:
    """

    result = qa_pipeline(question=question, context=context)

    # Extract the snippet near the answer
    start = result["start"]
    end = result["end"]
    snippet = context[max(0, start - 60):min(len(context), end + 60)]

    return {
        "answer": result["answer"],
        "context": f"...{snippet.strip()}..."
    }
