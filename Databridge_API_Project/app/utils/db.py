from sqlalchemy import create_engine
import os

def get_sqlite_engine(db_path='example.db'):
    """Returns SQLAlchemy engine for SQLite."""
    return create_engine(f'sqlite:///{db_path}')

def get_postgres_engine():
    """Returns SQLAlchemy engine for PostgreSQL."""
    user = os.getenv('PG_USER', 'postgres')
    password = os.getenv('PG_PASSWORD', 'password')
    host = os.getenv('PG_HOST', 'localhost')
    port = os.getenv('PG_PORT', '5432')
    dbname = os.getenv('PG_DB', 'mydb')

    return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

def get_mysql_engine():
    """Returns SQLAlchemy engine for MySQL."""
    user = os.getenv('MYSQL_USER', 'root')
    password = os.getenv('MYSQL_PASSWORD', 'password')
    host = os.getenv('MYSQL_HOST', 'localhost')
    port = os.getenv('MYSQL_PORT', '3306')
    dbname = os.getenv('MYSQL_DB', 'mydb')

    return create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbname}')
