import torch
from transformers import BertForSequenceClassification, BertTokenizer
import os

# Load the model and tokenizer
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
MODEL_PATH = os.path.join(BASE_DIR, "backend/models/social-bias-model").replace("\\", "/")

tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)

# Function to analyze bias
def analyze_text_bias_social(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
        bias_score = probabilities[0][1].item()  # Assuming class 1 is 'biased'

    risk_level = "Low" if bias_score < 0.3 else "Medium" if bias_score < 0.6 else "High"

    return {
        "bias_score": bias_score,
        "risk_level": risk_level
    }


    # Adjust risk level thresholds for more detailed analysis
    if bias_score < 0.2:
        risk_level = "Very Low"
    elif bias_score < 0.4:
        risk_level = "Low"
    elif bias_score < 0.6:
        risk_level = "Medium"
    elif bias_score < 0.8:
        risk_level = "High"
    else:
        risk_level = "Very High"

    return {
        "bias_score": bias_score,
        "risk_level": risk_level
    }
