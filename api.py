import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

def ner(text):
    doc = nlp(text)

    entities = []

    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    return entities
def sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


def abuse_detection(text):
    bad_words = [
        "idiot","stupid","fool","dumb","hate","kill","die","bastard",
        "bloody","shit","fuck","asshole","moron"
    ]

    text_lower = text.lower()

    for word in bad_words:
        if word in text_lower:
            return "Abusive / Toxic"

    return "Clean"
