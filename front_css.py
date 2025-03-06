def get_css():
    return """
    <style>
        /* Modern theme colors */
        :root {
            --primary: #1E40AF;        /* Royal Blue */
            --secondary: #3B82F6;      /* Bright Blue */
            --accent: #60A5FA;         /* Light Blue */
            --surface: #F8FAFC;        /* Light Surface */
            --card: #FFFFFF;           /* White */
            --success: #059669;        /* Emerald */
            --error: #DC2626;          /* Red */
            --text: #1F2937;          /* Dark Text */
        }

        /* Base styling */
        .stApp {
            background: var(--surface) !important;
            margin-top: -100px !important;
        }

        .main-container {
            max-width: 1200px;  /* Reduced from 1400px for better centering */
            margin: -50px auto;  /* Added auto for horizontal centering */
            padding: -10px;  /* Reduced from 3rem */
            background: var(--card);
            border-radius: 24px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
            text-align: center;  /* Center all content */
        }

        /* Enhanced Header styling */
        .header-container {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            padding: 1.5rem 2rem;  /* Reduced from 3rem */
            border-radius: 24px;
            margin-bottom: 0rem;  /* Reduced from 3rem */
            text-align: center;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(30, 64, 175, 0.15);
        }

        .header-title {
            color: white;
            font-size: 3.5rem !important;  /* Reduced from 4.5rem */
            font-weight: 800;
            letter-spacing: -0.02em;
            margin-bottom: 1rem !important;  /* Reduced from 1.5rem */
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            background: linear-gradient(to right, #ffffff, #e2e8f0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .header-subtitle {
            font-size: 1.2rem;  /* Reduced from 1.4rem */
            font-weight: 400;
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.5;  /* Reduced from 1.8 */
            color: rgba(255, 255, 255, 0.9);
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
            position: relative;
            padding: 0 1rem;
        }

        .header-subtitle::before,
        .header-subtitle::after {
            content: '';
            position: absolute;
            height: 2px;
            width: 60px;
            background: rgba(255, 255, 255, 0.5);
            top: 50%;
            transform: translateY(-50%);
        }

        .header-subtitle::before {
            left: -30px;
        }

        .header-subtitle::after {
            right: -30px;
        }

        /* Elegant Upload Section */
        .upload-section {
            background: linear-gradient(145deg, var(--surface), white);
            border-radius: 20px;
            padding: 0rem 0rem;  /* Reduced from 4rem */
            margin: 10px;  /* Removed margin */
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .upload-section:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        }

        /* Style Streamlit uploader */
        [data-testid="stFileUploader"] {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
        }

        /* Hide default Streamlit elements */
        [data-testid="stFileUploader"] > div:first-child {
            display: none;
        }

        /* Results section */
        .results-grid {
            max-width: 1000px;
            margin: 0 auto;
            padding: 1rem;
        }

        .result-card {
            background: white;
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
            border: 1px solid rgba(0, 0, 0, 0.05);
            margin: 1rem auto;  /* Center cards */
            text-align: center;
        }

        /* PDF viewer */
        iframe {
            border: none;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
            background: white;
        }

        /* Modern Messages */
        .success-message {
            background: linear-gradient(145deg, var(--success), #10B981);
            color: white;
            padding: 1.25rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(5, 150, 105, 0.15);
            font-weight: 500;
        }

        .error-message {
            background: linear-gradient(145deg, var(--error), #EF4444);
            color: white;
            padding: 1.25rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(220, 38, 38, 0.15);
            font-weight: 500;
        }

        /* Download button */
        .download-btn-container {
    display: flex;
    justify-content: center;
}

.download-btn {
    background: linear-gradient(145deg, var(--primary), var(--secondary));
    color: white !important;  /* Force white text color */
    padding: 1.25rem 2rem;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(30, 64, 175, 0.15);
    text-decoration: none !important;  /* Remove underline */
    display: inline-block;
    width: 100%;
    text-align: center;
    max-width: 300px;  /* Limit button width */
    margin: 1rem auto;  /* Center button */
}

.download-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(30, 64, 175, 0.25);
    color: white !important;  /* Keep text white on hover */
}

.download-btn:visited {
    color: white !important;  /* Keep text white after visit */
}
        .download-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(30, 64, 175, 0.25);
            color: white !important;  /* Keep text white on hover */
        }

        .download-btn:visited {
            color: white !important;  /* Keep text white after visit */
        }

        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Horizontal Loader */
        .loader-container {
            width: 100%;
            height: 4px;
            background-color: rgba(59, 130, 246, 0.1);
            border-radius: 4px;
            overflow: hidden;
            position: relative;
            margin: 1rem 0;
        }

        .loader-bar {
            position: absolute;
            width: 40%;
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            border-radius: 4px;
            animation: loading 1.5s infinite ease-in-out;
        }

        @keyframes loading {
            0% {
                left: -40%;
            }
            100% {
                left: 100%;
            }
        }
    </style>
    """
