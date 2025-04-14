from flask import Flask, request, jsonify
from backend.nlp_utils import detect_clauses
from backend.summarize import summarize_text
from backend.db import save_doc
import pdfplumber

app = Flask(__name__)

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        return " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["file"]
    text = extract_text_from_pdf(file)
    summary = summarize_text(text)
    clause = detect_clauses(text)
    save_doc(text, summary, clause)
    return jsonify({
        "summary": summary,
        "clause_index": clause
    })

if __name__ == "__main__":
    app.run(debug=True)
