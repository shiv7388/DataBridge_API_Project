import pandas as pd
from flask import Blueprint, request, Response
from sqlalchemy import create_engine, text
from app.auth import require_token

sql_bp = Blueprint('sql', __name__)

engine = create_engine('sqlite:///example.db')  # Or use PostgreSQL/MySQL engine

@sql_bp.route('/api/sql/download', methods=['POST'])
@require_token
def download_table():
    data = request.json
    query = data.get('query')  # Custom SQL
    if not query:
        return {'error': 'Missing SQL query'}, 400

    try:
        df = pd.read_sql(text(query), engine)
        csv = df.to_csv(index=False)
        return Response(
            csv,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=data.csv'}
        )
    except Exception as e:
        return {'error': str(e)}, 500
