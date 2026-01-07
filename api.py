import os
import spacy
from textblob import TextBlob
from groq import Groq #
from dotenv import load_dotenv

load_dotenv()
# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load local models
nlp = spacy.load("en_core_web_sm")

def ner(text):
    doc = nlp(text)
    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

def sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0: return "Positive"
    elif polarity < 0: return "Negative"
    return "Neutral"

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