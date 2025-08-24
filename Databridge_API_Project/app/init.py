from app.routes.upload import upload_bp  # ✅ Add this line

def create_app():
    app = Flask(__name__)
    app.register_blueprint(snow_bp)
    app.register_blueprint(sql_bp)
    app.register_blueprint(upload_bp)  # ✅ Register the upload blueprint
    return app
