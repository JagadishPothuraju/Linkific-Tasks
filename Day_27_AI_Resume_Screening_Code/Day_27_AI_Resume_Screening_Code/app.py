import streamlit as st
from src.resume_analyzer import analyze_resume, extract_text_from_file

st.set_page_config(page_title="AI Resume Screening Demo", page_icon="📄", layout="wide")
st.title("AI Resume Screening System")
st.caption("Educational prototype • Human review required • Not for automated hiring decisions")

st.warning(
    "This demo provides a basic job-description relevance summary. "
    "It must not be used to automatically select or reject applicants. "
    "Review the original resume and all results yourself."
)

with st.sidebar:
    st.header("How it works")
    st.write("1. Upload a resume (PDF, DOCX or TXT).")
    st.write("2. Paste a job description.")
    st.write("3. Review matched skills and the similarity indicator.")
    st.write("4. Verify every result against the original resume.")

uploaded = st.file_uploader("Upload a resume", type=["pdf", "docx", "txt"])
job_description = st.text_area(
    "Paste the job description",
    height=220,
    placeholder="Example: We need a Python developer with SQL, machine learning, pandas and communication skills..."
)

if st.button("Analyze resume", type="primary", disabled=(uploaded is None or not job_description.strip())):
    try:
        resume_text = extract_text_from_file(uploaded)
        if not resume_text.strip():
            st.error("No readable text was found in the uploaded file.")
        else:
            result = analyze_resume(resume_text, job_description)
            st.subheader("Analysis summary")
            c1, c2, c3 = st.columns(3)
            c1.metric("Text similarity", f"{result['similarity_score']}%")
            c2.metric("Matched listed skills", len(result["matched_skills"]))
            c3.metric("Job skills not found", len(result["missing_skills"]))

            st.caption(
                "Similarity is a simple text-overlap indicator, not a probability of job success "
                "or a validated candidate ranking."
            )
            left, right = st.columns(2)
            with left:
                st.markdown("**Skills found in resume and job description**")
                st.write(", ".join(result["matched_skills"]) if result["matched_skills"] else "No listed skills matched.")
            with right:
                st.markdown("**Job-description skills not detected**")
                st.write(", ".join(result["missing_skills"]) if result["missing_skills"] else "All configured skills were detected.")
            st.markdown("**Extracted resume preview**")
            st.text(resume_text[:2500] + ("..." if len(resume_text) > 2500 else ""))
            st.info("Human review: verify skills, experience, context and any extraction errors before drawing conclusions.")
    except Exception as exc:
        st.error(f"Could not analyze this file: {exc}")

st.divider()
st.caption("Privacy note: this local demo does not save uploaded resume contents to a database. Avoid uploading real personal data during testing.")
