import os
import sys
import logging
from flask_cors import CORS
from flask import Flask
from dotenv import load_dotenv

from .extensions import db, migrate

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Cấu hình CORS
    CORS(
        app,
        resources={r"/api/*": {
            "origins": [
                "http://localhost:5173",
                "http://127.0.0.1:5173",
                "http://localhost:5174",
                "http://127.0.0.1:5174"
            ]
        }}
    )

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

    # Import models
    from . import models

    from .routes.survey_routes import survey_bp
    app.register_blueprint(survey_bp, url_prefix="/api/surveys")

    @app.get("/health")
    def health():
        return {"status": "ok", "message": "L8 API is running"}, 200
    
    from src.routes.report_routes import report_bp
    app.register_blueprint(report_bp, url_prefix="/api/v1/reports/csat-nps")

    return app