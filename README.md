# 🤖 AI Resume Screening Agent

An AI-powered Resume Screening Agent built with **Python** and **Streamlit** that automatically analyzes resumes against a job description and calculates a match score based on relevant keywords.

## 🚀 Features

- 📄 Extracts text from PDF resumes using PyMuPDF
- 📝 Reads and analyzes job descriptions
- 🎯 Calculates resume-job match score
- 📊 Displays matched keywords and total keywords
- 🌐 Interactive web interface using Streamlit
- ⚡ Fast and easy resume screening

---

## 🛠️ Tech Stack

- Python
- Streamlit
- PyMuPDF (fitz)
- Regular Expressions (re)

---

## 📁 Project Structure

```
AI-Resume-Screening-Agent/
│
├── app.py
├── scorer.py
├── resume_parser.py
├── requirements.txt
├── README.md
│
├── jd/
│   └── job_description.txt
│
├── resumes/
│   └── sample_resume.pdf
│
├── output/
│
└── assets/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/parveenbhanu2005/AI-Resume-Screening-Agent.git
```

Move into the project folder:

```bash
cd AI-Resume-Screening-Agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Launch the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 📌 How to Use

1. Add your resume PDF to the **resumes/** folder.
2. Add the job description to **jd/job_description.txt**.
3. Run the Streamlit application.
4. Click **Analyze Resume**.
5. View:
   - Resume Match Score
   - Match Status
   - Matched Keywords
   - Total Keywords

---

## 📷 Sample Output

- ✅ Resume Match Score
- ✅ Progress Bar
- ✅ Match Status
- ✅ Matched Keywords
- ✅ Total Keywords

---

## 🔮 Future Improvements

- Multiple resume screening
- AI-based semantic matching
- Skill extraction using NLP
- Candidate ranking
- Resume upload through UI
- Export results to Excel/PDF

---

## 👨‍💻 Author

**Parveen Bhanu B**

GitHub: https://github.com/parveenbhanu2005

LinkedIn: *(Add your LinkedIn profile here)*

---

## 📄 License

This project is licensed under the MIT License.
