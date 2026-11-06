import streamlit as st
from src.resume_analyzer import ResumeProcessingError, analyze_resume, extract_text_from_file

st.set_page_config(page_title="AI Resume Screening Demo",page_icon="📄",layout="wide")
st.title("AI Resume Screening System")
st.caption("Educational prototype | Human review required")
st.warning("This text comparison must not be used to automatically select, rank or reject applicants.")
with st.sidebar:
    st.header("Workflow")
    st.write("1. Upload PDF, DOCX or TXT.\\n2. Paste a job description.\\n3. Review detected skills.\\n4. Verify against the original resume.")
    st.caption("Maximum file size: 5 MB.")
upload=st.file_uploader("Upload resume",type=["pdf","docx","txt"])
jd=st.text_area("Job description",height=220)
if st.button("Analyze resume",type="primary",disabled=upload is None or not jd.strip()):
    try:
        text=extract_text_from_file(upload,upload.name)
        result=analyze_resume(text,jd)
        a,b,c=st.columns(3)
        a.metric("Text similarity",f"{result['similarity_score']}%")
        b.metric("Matched skills",len(result["matched_skills"]))
        c.metric("Skills not detected",len(result["missing_skills"]))
        st.caption("Similarity measures text overlap, not job suitability.")
        left,right=st.columns(2)
        with left:
            st.markdown("**Matched skills**"); st.write(", ".join(result["matched_skills"]) or "No configured skills matched.")
        with right:
            st.markdown("**Job skills not detected**"); st.write(", ".join(result["missing_skills"]) or "All configured skills detected.")
        with st.expander("Extracted resume text"): st.text(text[:3000])
        st.info("A human reviewer must verify the original resume and all results.")
    except (ResumeProcessingError,ValueError,TypeError) as exc: st.error(str(exc))
    except Exception: st.error("Unexpected error. Check the file and try again.")
st.caption("Use synthetic sample data. Uploaded content is not intentionally saved by this demo.")
