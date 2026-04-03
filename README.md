# MCQ Web Quiz

A **Flask web application** that automatically generates **MCQs from PDFs**. Perfect for students and teachers for **quiz preparation**.

**Features:**

* Upload multiple PDFs into the `mcqs/` folder.
* Automatically extract questions, options, and answers.
* Click-to-show-answer for each MCQ.
* Collapsible PDF sections for better navigation.
* Parentheses in questions (e.g., `(DBMS)`) are removed automatically.

---

## Project Structure

```
MCQ-Web-Quiz/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md              # Project instructions
├── mcqs/                  # Folder where PDFs are placed
│   ├── pdf1.pdf
│   └── pdf2.pdf
├── templates/
│   └── index.html         # HTML template for MCQs
└── static/
    └── style.css          # CSS styling
```

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/MCQ-Web-Quiz.git
cd MCQ-Web-Quiz
```

---

## Step 2: Install Python Dependencies

It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 3: Add Your PDFs

* Place all your PDFs in the `mcqs/` folder.
* PDF format should be like:

```
1. (Subject) Question text
A) Option1 B) Option2 C) Option3 D) Option4
Answer: A
```

> Note: Parentheses in the question (like `(DBMS)`) are automatically removed when displayed.

---

## Step 4: Run the Application

```bash
python app.py
```

* Open your browser at: `http://127.0.0.1:5000/`
* You will see a list of PDFs.
* Click on a PDF to **expand/collapse** its MCQs.
* Click an **option** to show the answer (green for correct, red for wrong).

---

## Step 5: Using the App

1. Click on a PDF name to expand its questions.
2. Click any option to see the correct answer.
3. Repeat for other PDFs.

---

## Step 6: Optional Enhancements

* Add a **web upload feature** to allow PDFs to be uploaded directly from the browser.
* Add **search/filter MCQs** by keywords.
* Save **MCQs as CSV or PDF** for offline study.

---

