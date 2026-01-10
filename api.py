import os
import spacy
from textblob import TextBlob
from groq import Groq #
from dotenv import load_dotenv
from qa_utils.extractor import extract_text
from qa_utils.chunker import chunk_text
from qa_utils.qa_model import answer_question

load_dotenv()
# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load local models
nlp = spacy.load("en_core_web_sm")

def ner(text):
    doc = nlp(text)
    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

def sentiment(text):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a sentiment analysis system. "
                        "Analyze the text and respond with exactly one word only:\n"
                        "'Positive', 'Negative', or 'Neutral'."
                    )
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.0
        )

        result = chat_completion.choices[0].message.content.strip()

        if "Positive" in result:
            return "Positive"
        elif "Negative" in result:
            return "Negative"
        else:
            return "Neutral"

    except Exception as e:
        print(f"Groq API Error: {e}")
        return "API Error"

def abuse_detection(text):
    try:
        # Use Chat Completion to detect abuse
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a content moderator. Analyze the text and respond with exactly one word: 'Abusive' if it contains hate speech, insults, or threats, or 'Clean' if it is safe."
                },
                {
                    "role": "user",
                    "content": text,
                }
            ],
            model="llama-3.3-70b-versatile", # High-performance model
            temperature=0.0, # Keeps output consistent
        )

        # Extract the single-word response
        result = chat_completion.choices[0].message.content.strip()
        
        if "Abusive" in result:
            return "Abusive / Toxic Content Detected"
        return "Clean Content"

    except Exception as e:
        print(f"Groq API Error: {e}")
        return "API Error"
    

def document_qa(file_path, file_type, question):
    text = extract_text(file_path, file_type)

    if not text:
        return {"error": "Could not extract text"}

    chunks = chunk_text(text)
    result = answer_question(question, chunks)

    return {
        "answer": result["answer"],
        "confidence": round(result["score"], 3)
    }