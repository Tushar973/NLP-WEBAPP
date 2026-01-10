import pdfplumber
from docx import Document

def extract_text(file_path, file_type):
    text = ""

    if file_type == "pdf":
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"

    elif file_type == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    elif file_type == "docx":
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"

    return text.strip()
