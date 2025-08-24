import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.auth import require_token

upload_bp = Blueprint('upload', __name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@upload_bp.route('/api/upload', methods=['POST'])
@require_token
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    return jsonify({
        'message': 'File uploaded successfully',
        'filename': filename
    })
