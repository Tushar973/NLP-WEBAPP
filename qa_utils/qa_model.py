import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def answer_question(question, chunks):
    best_answer = None

    for chunk in chunks[:8]:
        prompt = f"""
You are a document question answering assistant.

Context:
{chunk}

Question:
{question}

Answer clearly and concisely using the context.
If the answer truly does not exist, reply exactly with:
NOT_FOUND
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        answer = response.choices[0].message.content.strip()

        print("RAW ANSWER:", answer)

        # ✅ ONLY reject if model explicitly says NOT_FOUND
        if answer != "NOT_FOUND":
            best_answer = answer
            break

    if best_answer:
        return {"answer": best_answer, "score": 1}

    return {"answer": "No answer found in the document.", "score": 0}

