from flask import Blueprint, request, jsonify
from models.bias_detector import analyze_text_bias
from models.sentiment_analysis import analyze_sentiment

analysis_bp = Blueprint("analysis", __name__)

@analysis_bp.route("/analyze-bias", methods=["POST"])
def analyze_bias():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    bias_result = analyze_text_bias(text)
    return jsonify(bias_result)

@analysis_bp.route("/analyze-sentiment", methods=["POST"])
def analyze_sentiment_route():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    sentiment_result = analyze_sentiment(text)
    return jsonify(sentiment_result)
