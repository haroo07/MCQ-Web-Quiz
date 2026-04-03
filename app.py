# from flask import Flask, render_template
# import pdfplumber
# import re
# import os

# app = Flask(__name__)

# PDF_FOLDER = "mcqs"  # folder containing your PDFs

# def extract_mcqs(pdf_path):
#     mcqs = []
#     text = ""
#     # Extract text from PDF
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             page_text = page.extract_text()
#             if page_text:
#                 text += page_text + "\n"

#     # Regex pattern for single-line options format (A) B) C) D))
#     pattern = r"(\d+)\.\s*(.*?)\s*A\)\s*(.*?)\s*B\)\s*(.*?)\s*C\)\s*(.*?)\s*D\)\s*(.*?)\s*Answer:\s*([A-Da-d])"
#     matches = re.findall(pattern, text, re.DOTALL)

#     for m in matches:
#         mcqs.append({
#             "q": m[1].strip(),
#             "options": [m[2].strip(), m[3].strip(), m[4].strip(), m[5].strip()],
#             "answer": {
#                 "A": m[2].strip(), "B": m[3].strip(), "C": m[4].strip(), "D": m[5].strip(),
#                 "a": m[2].strip(), "b": m[3].strip(), "c": m[4].strip(), "d": m[5].strip()
#             }[m[6].strip()]
#         })
#     return mcqs

# @app.route("/")
# def home():
#     all_mcqs = {}
#     pdf_files = sorted(os.listdir(PDF_FOLDER))
#     for pdf_file in pdf_files:
#         if pdf_file.lower().endswith(".pdf"):
#             path = os.path.join(PDF_FOLDER, pdf_file)
#             mcqs = extract_mcqs(path)
#             if mcqs:
#                 all_mcqs[pdf_file] = mcqs
#     return render_template("index.html", all_mcqs=all_mcqs)

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template
import pdfplumber
import re
import os

app = Flask(__name__)

PDF_FOLDER = "mcqs"  # folder containing your PDFs

def extract_mcqs(pdf_path):
    mcqs = []
    text = ""
    # Extract text from PDF
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # Regex pattern for single-line options format (A) B) C) D))
    pattern = r"(\d+)\.\s*(.*?)\s*A\)\s*(.*?)\s*B\)\s*(.*?)\s*C\)\s*(.*?)\s*D\)\s*(.*?)\s*Answer:\s*([A-Da-d])"
    matches = re.findall(pattern, text, re.DOTALL)

    for m in matches:
        # Remove parentheses content from question text
        clean_question = re.sub(r"\(.*?\)", "", m[1]).strip()

        mcqs.append({
            "q": clean_question,
            "options": [m[2].strip(), m[3].strip(), m[4].strip(), m[5].strip()],
            "answer": {
                "A": m[2].strip(), "B": m[3].strip(), "C": m[4].strip(), "D": m[5].strip(),
                "a": m[2].strip(), "b": m[3].strip(), "c": m[4].strip(), "d": m[5].strip()
            }[m[6].strip()]
        })
    return mcqs

@app.route("/")
def home():
    all_mcqs = {}
    pdf_files = sorted(os.listdir(PDF_FOLDER))
    for pdf_file in pdf_files:
        if pdf_file.lower().endswith(".pdf"):
            path = os.path.join(PDF_FOLDER, pdf_file)
            mcqs = extract_mcqs(path)
            if mcqs:
                all_mcqs[pdf_file] = mcqs
    return render_template("index.html", all_mcqs=all_mcqs)

if __name__ == "__main__":
    app.run(debug=True)