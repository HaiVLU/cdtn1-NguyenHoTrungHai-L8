import os
from flask import Flask
from dotenv import load_dotenv

from .extensions import db, migrate

load_dotenv()


def create_app():
    app = Flask(__name__)

    # Giữ nguyên tiếng Việt có dấu khi trả về JSON
    app.json.ensure_ascii = False

    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY", "local-development-key"
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if not app.config["SQLALCHEMY_DATABASE_URI"]:
        raise RuntimeError("Chưa cấu hình DATABASE_URL trong file .env")

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models để Flask-Migrate nhận diện các bảng
    from . import models

    from .routes.survey_routes import survey_bp
    app.register_blueprint(survey_bp, url_prefix="/api/surveys")

    @app.get("/health")
    def health():
        return {"status": "ok", "message": "L8 API is running"}, 200

    return app