from flask import Blueprint, request, jsonify
from models.bias_detector import analyze_text_bias
from models.sentiment_analysis import analyze_sentiment

scorecard_bp = Blueprint("scorecard", __name__)

@scorecard_bp.route("/generate-scorecard", methods=["POST"])
def generate_scorecard():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    bias_result = analyze_text_bias(text)
    sentiment_result = analyze_sentiment(text)

    bias_score = bias_result.get("bias_score", 0)
    sentiment_score = sentiment_result.get("sentiment_score", 0)

    ethical_score = (bias_score + sentiment_score) / 2
    risk_level = "Low" if ethical_score >= 0.7 else "Medium" if ethical_score >= 0.4 else "High"

    return jsonify({
        "bias_score": bias_score,
        "sentiment_score": sentiment_score,
        "ethical_score": ethical_score,
        "risk_level": risk_level
    })
