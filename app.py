import streamlit as st
from resume_parser import extract_text_from_pdf
from scorer import calculate_score
import os

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Screening Agent")
st.write("Upload a resume and compare it with a Job Description.")

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Analyze Resume"):

    if uploaded_resume is None:
        st.error("Please upload a resume.")
    elif job_description.strip() == "":
        st.error("Please enter the Job Description.")
    else:

        os.makedirs("resumes", exist_ok=True)

        resume_path = os.path.join("resumes", uploaded_resume.name)

        with open(resume_path, "wb") as f:
            f.write(uploaded_resume.getbuffer())

        resume_text = extract_text_from_pdf(resume_path)

        score, matched, total = calculate_score(
            resume_text,
            job_description
        )

        st.success("Analysis Complete!")

        st.metric("Resume Match Score", f"{score}%")

        st.progress(int(score))

        if score >= 80:
            st.success("Excellent Match ✅")
        elif score >= 60:
            st.warning("Good Match 🟡")
        elif score >= 40:
            st.warning("Average Match 🟠")
        else:
            st.error("Poor Match ❌")

        st.write(f"Matched Keywords: **{matched}**")
        st.write(f"Total Keywords: **{total}**")