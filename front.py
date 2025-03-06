import streamlit as st
import requests
import os
from PyPDF2 import PdfReader
from front_css import get_css
import time

# Set Streamlit page config
st.set_page_config(
    page_title="Ethic Guard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS
st.markdown(get_css(), unsafe_allow_html=True)

# Flask Backend URL and temp directory setup
BACKEND_URL = "http://localhost:5000"
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

# Main container with improved layout
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Enhanced Header with better formatting
st.markdown('''
    <div class="header-container">
        <h1 class="header-title">EthicGuard</h1>
        <div class="header-subtitle">
            Transform your documents with AI-powered ethical analysis.<br>
            Ensuring compliance and fairness in every word.
        </div>
    </div>
''', unsafe_allow_html=True)

# Upload Section
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
st.markdown('''
    <div style="margin-bottom: 1.5rem;">
        <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
            <polyline points="17 8 12 3 7 8"/>
            <line x1="12" y1="3" x2="12" y2="15"/>
        </svg>
    </div>
    <h3 style="color: #1E40AF; margin-bottom: 0.5rem;">Upload Your Document</h3>
    <p style="color: #6B7280; margin-bottom: 2rem;">Drag and drop your PDF file or click to browse</p>
''', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# Process uploaded file (if any)
if uploaded_file is not None:
    temp_path = os.path.join(TEMP_DIR, uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    # Create progress bar and status message
    progress_bar = st.progress(0)
    status = st.empty()
    
    try:
        # Stage 1: Processing PDF
        status.markdown("🔄 Processing the PDF...")
        for i in range(0, 30):
            time.sleep(0.02)
            progress_bar.progress(i)
            
        # Start the API request
        files = {'pdf-file': open(temp_path, 'rb')}
        
        # Stage 2: Analyzing Content
        status.markdown("🔍 Analyzing document content...")
        for i in range(30, 70):
            time.sleep(0.03)
            progress_bar.progress(i)
        
        # Make the API call
        response = requests.post(f"{BACKEND_URL}/process-pdf", files=files)
        
        # Stage 3: Finalizing Analysis
        status.markdown("✨ Finalizing analysis...")
        for i in range(70, 100):
            time.sleep(0.02)
            progress_bar.progress(i)
        
        # Complete
        progress_bar.progress(100)
        status.markdown("✅ Analysis complete!")
        time.sleep(0.5)
        
        # Clear progress elements
        progress_bar.empty()
        status.empty()
        
        if response.status_code == 200:
            st.markdown('''
                <div class="success-message">
                    ✨ Document processed successfully!
                </div>
            ''', unsafe_allow_html=True)
            
            # Results section with improved layout
            st.markdown('<div class="results-grid">', unsafe_allow_html=True)
            
            # Single column layout for PDF viewer and download button
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("### 📑 Processed Document")
            output_url = response.json().get("output_pdf_url")
            st.markdown(f'<iframe src="{BACKEND_URL}{output_url}" width="100%" height="600"></iframe>', unsafe_allow_html=True)
            
            # Download button below PDF
            st.markdown(f'''
                <div class="download-btn-container">
                <a href="{BACKEND_URL}{output_url}" class="download-btn" download>
                    📥 Download Processed PDF
                </a>
                </div>
            ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('''
                <div class="error-message">
                    ❌ Error processing document. Please try again.
                </div>
            ''', unsafe_allow_html=True)
            
    except requests.exceptions.RequestException as e:
        # Clear progress bar on error
        progress_bar.empty()
        st.markdown(f'''
            <div class="error-message">
                ❌ Connection error: {str(e)}
                <br>Please make sure the backend server is running.
            </div>
        ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
