from flask import Blueprint, request, jsonify
from models.policy_generator import generate_policy

policy_bp = Blueprint("policy", __name__)

@policy_bp.route("/generate-policy", methods=["POST"])
def generate_policy_route():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    policy_result = generate_policy(text)
    return jsonify(policy_result)
