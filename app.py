import streamlit as st
from resume_parser import extract_resume_text
from skill_matcher import match_resume_job, missing_skills

st.title("AI Resume Analyzer")

st.write("Upload your resume and compare it with a job description.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste Job Description")

skills_list = [
    "Python",
    "C",
    "C++",
    "Machine Learning",
    "SQL",
    "Linux",
    "Data Structures",
    "Git",
]

if uploaded_file is not None and job_description != "":

    resume_text = extract_resume_text(uploaded_file)

    score = match_resume_job(resume_text, job_description)

    st.subheader("Resume Match Score")
    st.success(f"{score}% Match")

    missing = missing_skills(resume_text, skills_list)

    st.subheader("Recommended Skills to Add")

    if len(missing) == 0:
        st.write("Your resume already includes all important skills.")
    else:
        for skill in missing:
            st.write(f"- {skill}")