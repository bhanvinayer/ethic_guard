from social_bias_detector import analyze_text_bias_social

# List of example texts to analyze for bias
texts = [
    "The leftist agenda is brainwashing the younger generation."
]

# Analyze bias for each text
for text in texts:
    bias_result = analyze_text_bias_social(text)
    print(f"Text: {text}")
    print(f"Bias Score: {bias_result['bias_score']:.4f}")
    print(f"Risk Level: {bias_result['risk_level']}\n")
