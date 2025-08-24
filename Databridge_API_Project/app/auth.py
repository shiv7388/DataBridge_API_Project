from flask import request, jsonify
from functools import wraps

VALID_TOKEN = 'supersecrettoken'

def require_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token != f'Bearer {VALID_TOKEN}':
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated
