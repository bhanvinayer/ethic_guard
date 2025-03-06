from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
from routes.analysis import analysis_bp
from routes.policy import policy_bp
from routes.scorecard import scorecard_bp
from models.process_pdf import process_pdf

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Enable CORS
CORS(app)

# Register blueprints (routes)
app.register_blueprint(analysis_bp, url_prefix="/api")
app.register_blueprint(policy_bp, url_prefix="/api")
app.register_blueprint(scorecard_bp, url_prefix="/api")

# Root route
@app.route("/")
def home():
    return {"message": "AI Ethical Review System is running!"}

@app.route('/process-pdf', methods=['POST'])
def process_pdf_endpoint():
    if 'pdf-file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['pdf-file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    input_pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    output_pdf_path = os.path.join(app.config['PROCESSED_FOLDER'], filename)

    file.save(input_pdf_path)
    process_pdf(input_pdf_path, output_pdf_path)

    return jsonify({'output_pdf_url': f'/processed/{filename}'})

@app.route('/processed/<filename>')
def download_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)
    app.run(debug=True, port=5000)
