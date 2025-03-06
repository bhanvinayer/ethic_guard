import os
from dotenv import load_dotenv

load_dotenv()

# Configurations
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
SECRET_KEY = os.getenv("SECRET_KEY")
MODEL_PATH = os.getenv("MODEL_PATH", "./backend/models/bias_detection_model")
