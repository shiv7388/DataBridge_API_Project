import snowflake.connector
from flask import Blueprint, request, jsonify
from app.auth import require_token

snow_bp = Blueprint('snowflake', __name__)

@snow_bp.route('/api/snowflake/procedure', methods=['POST'])
@require_token
def call_proc():
    data = request.json
    proc_name = data.get('proc')
    params = data.get('params', [])

    try:
        conn = snowflake.connector.connect(
            user='...', password='...', account='...',
            warehouse='...', database='...', schema='...'
        )
        cur = conn.cursor()
        result = cur.callproc(proc_name, params)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
