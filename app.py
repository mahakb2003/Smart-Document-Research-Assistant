# app.py
''' import streamlit as st
import os
from backend.parser import extract_text_from_pdf, extract_text_from_txt
from backend.summarizer import summarize_text

# Set UI title
st.title("Smart Assistant for Research Summarization")

# Upload section
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    # Save file to /data/
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_txt(file_path)

    # Show success and summary
    st.success("✅ File uploaded and text extracted successfully!")
    with st.spinner("Summarizing..."):
        summary = summarize_text(text)

    st.subheader(" Document Summary (≤ 150 words):")
    st.write(summary)'''

# app.py
import streamlit as st
import os
import time
from backend.parser import extract_text_from_pdf, extract_text_from_txt
from backend.summarizer import summarize_text
from backend.qa_engine import answer_question  # Make sure this exists and is correct
from backend.gemini_utils import gemini_answer
from backend.gemini_utils import gemini_answer, generate_challenge_questions, evaluate_user_answer



# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Smart Document Assistant",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---- CUSTOM STYLING ----
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }

    body {
        background-color: #0f0f0f;
    }

    .main-container {
        background-color: #ffffff;
        padding: 40px 30px;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .title {
        font-size: 40px;
        font-weight: bold;
        color: #005f99;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 20px;
        color: #333333;
        text-align: center;
        margin-bottom: 30px;
    }

    .summary-heading {
        font-size: 22px;
        font-weight: 700;
        color: #004080;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    .summary-text {
        font-size: 16px;
        color: #1c1c1c;
        background-color: #e6f2ff;
        padding: 20px;
        border-radius: 10px;
        line-height: 1.6;
    }

    .stFileUploader label {
        font-size: 16px;
        font-weight: bold;
        color: #000000;
    }

    .stExpanderHeader {
        font-size: 16px;
        font-weight: bold;
        color: #005f99;
    }
    </style>

    <div class="main-container">
    """,
    unsafe_allow_html=True
)

# ---- HEADER SECTION ----
st.markdown('<div class="title">Smart Research Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload your PDF or TXT file and get a smart summary instantly!</div>', unsafe_allow_html=True)

# ---- FILE UPLOAD SECTION ----
uploaded_file = st.file_uploader("Choose a file to summarize", type=["pdf", "txt"])

if uploaded_file:
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_txt(file_path)

    # Preview Extracted Text
    with st.expander("Preview Extracted Text", expanded=False):
        st.write(text[:1000] + "...")

    # Spinner and Summary
    with st.spinner("📘 Reading, thinking, and summarizing..."):
        time.sleep(3)
        summary = summarize_text(text)

    # Final Output
    st.markdown('<div class="summary-heading">📌 Here is your summarized text:</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="summary-text">{summary}</div>', unsafe_allow_html=True)

    # ---- INTERACTION MODES ----
    mode = st.radio("Choose Interaction Mode:", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        user_question = st.text_input("Ask a question based on the document:")

        if user_question:
            with st.spinner("🤖 Thinking with Gemini..."):
                prompt = f"Answer this question based on the following document:\n\n{summary}\n\nQuestion: {user_question}"
                response = gemini_answer(prompt)

            st.markdown("### 🧠 Answer:")
            st.write(response)

            st.markdown("### 📌 Justification from Document:")
            st.markdown(f'<div class="summary-text">{summary}</div>', unsafe_allow_html=True)


    elif mode == "Challenge Me":
        st.markdown("### 🧠 Challenge Mode: Test your understanding!")

        if text:  # check that document was uploaded and text is available
            with st.spinner("📘 Generating challenge questions..."):
                # Clean and extract exactly 3 valid lines
                challenge_output = generate_challenge_questions(text)

# Split and clean non-empty questions that start with "Q" or a number
                questions = challenge_output
# Take only top 3 valid questions
                questions = questions[:3]


        # Ensure we only take 3 questions
                questions = questions[:3]
            user_answers = []
            for idx, question in enumerate(questions, start=1):
                st.markdown(f"**Q{idx}. {question}**")
                answer = st.text_input(f"Your Answer to Q{idx}", key=f"user_answer_{idx}")
                user_answers.append((question, answer))

            if st.button("Submit Answers"):
                st.markdown("###  Evaluation:")
                for i, (question, user_ans) in enumerate(user_answers):
                    if user_ans.strip():  # only evaluate if user gave an answer
                        with st.spinner(f"Evaluating your answer for Q{i+1}..."):
                            feedback = evaluate_user_answer(text, question, user_ans)
                            st.markdown(f"**Q{i+1}. {question}**")
                            st.markdown(f" **Your Answer:** {user_ans}")
                            max_lines = 6
                            trimmed_feedback = "\n".join(feedback.splitlines()[:max_lines])
                            if len(trimmed_feedback) > 600:
                                trimmed_feedback = trimmed_feedback[:600] + "..."
                            st.markdown(f"🔍 **Feedback:** {trimmed_feedback}")
                    else:
                        st.warning(f"⚠️ Please answer Q{i+1} before submitting.")



# ---- CLOSE CONTAINER DIV ----
st.markdown("</div>", unsafe_allow_html=True)
