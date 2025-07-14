
#  🤖 Smart-Document-Research-Assistant


A GenAI-powered assistant that reads, understands, and interacts with documents like research papers, technical manuals, or legal files. Users can upload a PDF/TXT, get an instant summary, ask contextual questions, and challenge themselves with comprehension-based questions—all powered by Google Gemini API.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Features

- 📄 **Upload PDF/TXT Files**  
  Upload structured English documents like research papers, manuals, or reports.

- 🧠 **Ask Anything Mode**  
  Ask free-form questions and get document-grounded answers with justifications.

- 🎯 **Challenge Me Mode**  
  Auto-generates logic-based questions from the document and evaluates your answers.

- 📝 **Smart Summary (≤ 150 Words)**  
  Generates a concise summary immediately after upload.

- ✅ **Document-Grounded Responses**  
  Every answer is backed with evidence from the original document.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠 Tech Stack Used

| Component              | Technology Used                   |
|------------------------|-----------------------------------|
| 📦 Frontend UI         | `Streamlit`                       |
| 📂 File Parsing        | `PyMuPDF` for PDFs, basic file IO |
| 📚 Summarization       | `Gemini 1.5 Flash (Google API)`   |
| 💬 QA & Evaluation     | `Gemini 1.5 Flash (Google API)`   |
| 🔐 Environment Config  | `python-dotenv`, `.env` file      |
| 🧠 Logic Generation    | Gemini prompt engineering         |
| 🗂 Directory Structure | Modular Python architecture       |

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📁 Project Structure
smart-doc-assistant/
1. app.py # Main Streamlit app

2. .env # Gemini API Key (ignored in Git)

3. backend

3.1 parser.py # Extract text from PDFs/TXTs

3.2 summarizer.py # Summarization logic

3.3 qa_engine.py # Challenge evaluation logic

3.4 gemini_utils.py # Gemini API functions

4.README.md # This file


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🧪 How It Works

1. **Upload** a PDF/TXT document.
2. App **extracts and summarizes** the content.
3. Choose:
   - **Ask Anything**: Ask a question → Get a Gemini-powered answer with justification.
   - **Challenge Me**: AI generates 3 logic-based questions → You answer → AI gives feedback.
4. All responses are grounded in the actual uploaded document.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🧰 Installation & Setup

git clone https://github.com/your-username/smart-doc-assistant.git
cd smart-doc-assistant
pip install -r requirements.txt

🙌 Credits
Developed by Mahak Bisht
Data Science Intern Applicant – EZ Campus Drive 2025

