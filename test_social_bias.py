import torch
from transformers import BertTokenizer
from models.social_bias_detector import analyze_text_bias

# Load the model and tokenizer
MODEL_PATH = os.path.join(BASE_DIR, "backend/models/social-bias-model").replace("\\", "/")

tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = torch.load(MODEL_PATH)

# List of example texts to analyze for bias
texts = [
    "Men are better leaders than women.",
    "All races should be treated equally.",
    "Women are not as good at math as men.",
    "Everyone deserves equal opportunities regardless of their background."
]

# Analyze bias for each text
for text in texts:
    bias_result = analyze_text_bias(text)
    print(f"Text: {text}")
    print(f"Bias Score: {bias_result['bias_score']:.4f}")
    print(f"Risk Level: {bias_result['risk_level']}\n")
