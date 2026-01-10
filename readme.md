# 🧠 NLP Web Application  
### Sentiment Analysis • Abuse Detection • Named Entity Recognition • Document Question Answering

`Python 3.10+` • `Flask` • `spaCy` • `TextBlob` • `Groq API` • `HTML/CSS`


---

## 🚀 Overview

Natural Language Processing (NLP) applications are widely used to analyze user-generated text, but many beginner systems lack proper structure, clarity, and usability.

This project is a **full-stack NLP web application** that provides **Sentiment Analysis**, **Abuse/Toxicity Detection**, **Named Entity Recognition (NER)**, and **Document-based Question Answering** through a **secure Flask-based web interface** with session-based authentication.

The project demonstrates **end-to-end NLP engineering**, covering backend logic, NLP inference, authentication, and frontend rendering.


---

## ✨ Key Features

- 🔐 **User Authentication**
  - Register & Login system
  - Password Hashing Feature
  - Session-based protected routes

- 😊 **Sentiment Analysis**
  - Classifies text as **Positive / Negative / Neutral**
  - Implemented using Groq api

- 🚫 **Abuse / Toxicity Detection**
  - Detects offensive or toxic words using Groq api
  - Returns `Abusive / Toxic` or `Clean`

- 🏷️ **Named Entity Recognition (NER)**
  - Extracts entities like **PERSON**, **ORG**, **GPE**, **DATE**
  - Powered by spaCy (`en_core_web_sm`)

- 📄 **Document Question Answering**
  - Allows users to upload documents (PDF / TXT / DOCX)
  - Answers natural-language questions based on document content
  - Implemented using transformer / LLM-based QA models via API

- 🎨 **Modern UI**
  - Clean, responsive HTML/CSS pages
  - Gradient-based design for better UX

---

## ⚙️ System Architecture

User  
└── Browser (UI)  
    └── Flask App  
        ├── Authentication Layer  
        │   └── JSON-based user store  
        │  
        └── NLP API Layer  
            ├── Sentiment Analysis (Groq API)  
            ├── Abuse / Toxicity Detection (Groq API)  
            ├── Named Entity Recognition (spaCy)  
            └── Document Question Answering  
                ├── Document Upload & Text Extraction  
                ├── Text Chunking  
                └── LLM-based QA Inference (Groq API)


---
## 🔍 NLP Processing Pipeline

1. **Text / Document Input**
   - User submits text via the web interface  
   - OR uploads a document (PDF / TXT / DOCX) for question answering  

2. **NLP Processing**
   - Sentiment Analysis → Text classification via Groq API  
   - Abuse Detection → Toxicity classification via Groq API  
   - NER → Entity extraction using spaCy  
   - Document Question Answering →  
     - Text extraction from document  
     - Text chunking  
     - LLM-based question answering using Groq API  

3. **Result Rendering**
   - Predictions and answers displayed instantly on the frontend



---

## 🧪 Example Behavior

| Task | Input | Output |
|----|------|-------|
| Sentiment | I love this product | Positive |
| Sentiment | This is terrible | Negative |
| Abuse Detection | You are stupid | Abusive / Toxic |
| Abuse Detection | Great work team | Clean |
| NER | Elon Musk founded SpaceX | PERSON, ORG |

---

## 🛠️ Tech Stack

| Component | Technology |
|---------|-----------|
| Backend | Python, Flask |
| NLP | spaCy, TextBlob, Groq API |
| Frontend | HTML, CSS |
| Authentication | Flask Sessions |
| Storage | JSON |
| Document Processing | pdfplumber, python-docx |
| Deployment Ready | Yes |

---

## 📁 Project Structure

nlp-webapp/
│
├── qa_utils/
│   ├── extractor.py        # Document text extraction
│   ├── chunker.py          # Text chunking logic
│   └── qa_model.py         # LLM-based Question Answering
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   ├── sentiment.html
│   ├── abuse.html
│   ├── ner.html
│   └── document-qa.html    # Document Question Answering UI
│
├── uploads/                # Temporarily stored documents
│
├── api.py                  # NLP logic
├── app.py                  # Flask routes & sessions
├── db.py                   # Authentication logic
├── users.json              # User data
├── requirements.txt
└── README.md

---

## 🔒 Authentication Flow

1. User registers → stored in users.json
2. Login validates email & password
3. Session created after successful login
4. NLP routes are protected

---

## 🔮 Future Improvements

1. Database integration (PostgreSQL / MongoDB)
2. REST API endpoints
3. Cloud deployment (Render / Railway / AWS)

---

## 👨‍💻 Author

Tushar Kumar Gautam
Electrical Engineering, IIT Roorkee
Interests: NLP, Machine Learning, Backend Development, Deep Learning, Generative AI, MLOPS



