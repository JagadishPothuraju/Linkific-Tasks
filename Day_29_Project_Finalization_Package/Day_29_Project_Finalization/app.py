import streamlit as st
from src.resume_analyzer import extract_text_from_bytes, analyze_resume

st.set_page_config(page_title="AI Resume Screening System", page_icon="📄", layout="wide")
st.title("AI Resume Screening System")
st.caption("Educational prototype • Human review is required")

uploaded = st.file_uploader("Upload resume", type=["pdf", "docx", "txt"])
jd = st.text_area("Paste job description", height=220, placeholder="Enter the job requirements here...")
if st.button("Analyze resume", type="primary"):
    if uploaded is None:
        st.error("Please upload a resume first.")
    elif not jd.strip():
        st.error("Please enter a job description.")
    else:
        try:
            resume_text = extract_text_from_bytes(uploaded.name, uploaded.getvalue())
            result = analyze_resume(resume_text, jd)
            st.subheader("Analysis results")
            st.metric("Text similarity", f"{result['similarity'] * 100:.1f}%")
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Matched JD skills**")
                st.write(result["matched_skills"] or ["No configured skill keywords matched"])
            with c2:
                st.markdown("**JD skills not found in resume**")
                st.write(result["missing_skills"] or ["No missing configured skills"])
            st.info("This score measures text similarity only. It is not a hiring recommendation. A human reviewer must assess context and evidence.")
        except Exception as exc:
            st.error(f"Could not analyze this resume: {exc}")
st.divider()
st.caption("Privacy: use only resumes you are authorized to process. Avoid storing personal data unnecessarily.")
