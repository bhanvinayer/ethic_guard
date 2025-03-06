from bias_detector import analyze_text_bias as analyze_text_bias_detector
from social_bias_detector import analyze_text_bias as analyze_text_social_bias

# List of example texts to analyze for bias
texts = [
    "Men are better leaders than women.",
    "All races should be treated equally.",
    "Women are not as good at math as men.",
    "Everyone deserves equal opportunities regardless of their background."
]

# Analyze bias for each text using both detectors
for text in texts:
    # Analyze using bias_detector
    bias_result_detector = analyze_text_bias_detector(text)
    print(f"Text: {text}")
    print(f"Bias Score (Detector): {bias_result_detector['bias_score']:.4f}")
    print(f"Risk Level (Detector): {bias_result_detector['risk_level']}")
    
    # Analyze using social_bias_detector
    bias_result_social = analyze_text_social_bias(text)
    print(f"Bias Score (Social): {bias_result_social['bias_score']:.4f}")
    print(f"Risk Level (Social): {bias_result_social['risk_level']}\n")
