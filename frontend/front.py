import streamlit as st
import requests
import os

# Set the title of the app
st.set_page_config(page_title="Ethic Guard", layout="wide")

# Flask Backend URL
BACKEND_URL = "http://localhost:5000"

# Ensure the "temp" directory exists
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Features", "Upload Document", "About"])

# Home page
if page == "Home":
    st.title("Welcome to Ethic Guard")
    st.write("Ethic Guard is your solution for ethical monitoring and compliance.")

# Features page
elif page == "Features":
    st.title("Features")
    st.write("Here are some of the features of Ethic Guard:")
    st.markdown("""
    - **Real-time Monitoring**: Keep track of activities in real-time.
    - **Compliance Reports**: Generate detailed compliance reports.
    - **Alerts and Notifications**: Get notified of any unethical activities.
    - **User Management**: Manage users and their roles.
    """)

# Upload Document page
elif page == "Upload Document":
    st.title("Upload Document")
    
    uploaded_file = st.file_uploader("Choose a document", type=["pdf", "docx", "txt"])
    
    if uploaded_file is not None:
        st.write(f"Uploading {uploaded_file.name}...")

        # Define file path
        temp_file_path = os.path.join(TEMP_DIR, uploaded_file.name)

        # Save uploaded file
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Send file to Flask backend
        with open(temp_file_path, "rb") as f:
            response = requests.post(f"{BACKEND_URL}/process-pdf", files={"pdf-file": f})

        # Handle response
        if response.status_code == 200:
            output_url = response.json().get("output_pdf_url")
            st.success("Document processed successfully!")
            st.markdown(f"📄 [Download Processed PDF]({BACKEND_URL}{output_url})")
        else:
            st.error("Failed to process document.")

# About page
elif page == "About":
    st.title("About Ethic Guard")
    st.write("Ethic Guard is developed to ensure ethical practices in organizations.")
    st.write("Version: 1.0.0")
    st.write("Developed by: Your Name")
