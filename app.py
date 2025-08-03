import streamlit as st
import os
from utils.extract_text import extract_text_from_pdf
from utils.keyword_extractor import extract_keywords
from utils.blooms_classifier import classify_blooms_level

# Setup folder
SAMPLE_SYLLABI_DIR = "sample_syllabi"
os.makedirs(SAMPLE_SYLLABI_DIR, exist_ok=True)

# Page Config
st.set_page_config(page_title="📘 Syllabus & Curriculum Optimizer", layout="wide")

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Choose Section", ["🏠 Home", "📤 Upload & Extract", "🔑 Keyword Analysis", "🎯 Bloom's Classification"])

st.title("📘 Syllabus & Curriculum Design Optimizer")

# Session state
if 'syllabus_text' not in st.session_state:
    st.session_state.syllabus_text = ""
if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False

# 🏠 Home
if page == "🏠 Home":
    st.markdown("""
        Welcome to the **Syllabus & Curriculum Design Optimizer** 🎓  
        This tool helps faculty and educators to:
        - 📤 Upload Syllabus PDFs  
        - 📄 Extract structured text  
        - 🔑 Identify key concepts  
        - 🎯 Classify learning objectives using **Bloom's Taxonomy**

        👉 Start by selecting **Upload & Extract** from the sidebar.
    """)

# 📤 Upload & Extract
elif page == "📤 Upload & Extract":
    st.subheader("📤 Upload Your Syllabus PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file:
        file_path = os.path.join(SAMPLE_SYLLABI_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("🔍 Extracting text from PDF..."):
            try:
                syllabus_text = extract_text_from_pdf(file_path)
                st.session_state.syllabus_text = syllabus_text
                st.session_state.file_uploaded = True
                st.success("✅ Text successfully extracted!")

                st.subheader("📄 Extracted Text Preview")
                st.text_area("Preview", syllabus_text[:3000] + "..." if len(syllabus_text) > 3000 else syllabus_text, height=300)
            except Exception as e:
                st.error(f"❌ Error extracting text: {e}")

# 🔑 Keyword Analysis
elif page == "🔑 Keyword Analysis":
    st.subheader("🔑 Extract Keywords")
    if st.session_state.file_uploaded:
        with st.spinner("🔍 Extracting keywords..."):
            keywords = extract_keywords(st.session_state.syllabus_text)
        st.success("✅ Keywords extracted!")
        st.write(", ".join(keywords))
    else:
        st.warning("⚠️ Please upload a syllabus first in 'Upload & Extract' tab.")

# 🎯 Bloom's Classification
elif page == "🎯 Bloom's Classification":
    st.subheader("🎯 Classify Learning Objectives by Bloom’s Levels")
    if st.session_state.file_uploaded:
        with st.spinner("🔍 Analyzing text..."):
            try:
                # Simple sentence splitter (alternative to nltk.sent_tokenize)
                sentences = st.session_state.syllabus_text.split('.')
                sentences = [s.strip() for s in sentences if s.strip()]
                bloom_results = classify_blooms_level(sentences)
            except Exception as e:
                st.error(f"❌ Failed to classify Bloom's levels: {e}")
                bloom_results = []

        if bloom_results:
            st.write("Bloom Results Preview:", bloom_results)
            for sentence, level in bloom_results:
                st.markdown(f"- **{sentence.strip()}** → 🧠 *{level}*")
        else:
            st.info("ℹ️ No learning objectives were found.")
    else:
        st.warning("⚠️ Please upload a syllabus first in 'Upload & Extract' tab.")
