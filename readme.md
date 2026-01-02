# 🧠 NLP Web Application  
### Sentiment Analysis • Abuse Detection • Named Entity Recognition

`Python 3.10+` • `Flask` • `spaCy` • `TextBlob` • `HTML/CSS`

---

## 🚀 Overview

Natural Language Processing (NLP) applications are widely used to analyze user-generated text, but many beginner systems lack proper structure, clarity, and usability.
This project is a **full-stack NLP web application** that provides **Sentiment Analysis**, **Abuse/Toxicity Detection**, and **Named Entity Recognition (NER)** through a **secure Flask-based web interface** with session-based authentication.
The project demonstrates **end-to-end NLP engineering**, covering backend logic, NLP inference, authentication, and frontend rendering.

---

## ✨ Key Features

- 🔐 **User Authentication**
  - Register & Login system
  - Session-based protected routes

- 😊 **Sentiment Analysis**
  - Classifies text as **Positive / Negative / Neutral**
  - Implemented using TextBlob polarity scoring

- 🚫 **Abuse / Toxicity Detection**
  - Detects offensive or toxic words
  - Returns `Abusive / Toxic` or `Clean`

- 🏷️ **Named Entity Recognition (NER)**
  - Extracts entities like **PERSON**, **ORG**, **GPE**, **DATE**
  - Powered by spaCy (`en_core_web_sm`)

- 🎨 **Modern UI**
  - Clean, responsive HTML/CSS pages
  - Gradient-based design for better UX

---

## ⚙️ System Architecture
User
└── Browser (UI)
└── Flask App
├── Authentication Layer
│ └── JSON-based user store
│
└── NLP API Layer
├── Sentiment Analysis (TextBlob)
├── Abuse Detection (Rule-based)
└── NER (spaCy)

---

## 🔍 NLP Processing Pipeline

1. **Text Input**
   - User submits text via the web interface

2. **NLP Processing**
   - Sentiment → Polarity computation
   - Abuse Detection → Keyword scanning
   - NER → Entity extraction via spaCy

3. **Result Rendering**
   - Output displayed instantly on the frontend

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
| NLP | spaCy, TextBlob |
| Frontend | HTML, CSS |
| Authentication | Flask Sessions |
| Storage | JSON |
| Deployment Ready | Yes |

---

## 📁 Project Structure
nlp-webapp/
│
├── templates/
│ ├── login.html
│ ├── register.html
│ ├── profile.html
│ ├── sentiment.html
│ ├── abuse.html
│ └── ner.html
│
├── api.py # NLP logic
├── app.py # Flask routes & sessions
├── db.py # Authentication logic
├── users.json # User data
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

1. Password hashing (bcrypt)
2. Database integration (PostgreSQL / MongoDB)
3. ML/DL-based abuse detection
4. REST API endpoints
5. Cloud deployment (Render / Railway / AWS)

---

## 👨‍💻 Author

Tushar Kumar Gautam
Electrical Engineering, IIT Roorkee
Interests: NLP, Machine Learning, Backend Development, Deep Learning, Generative AI



