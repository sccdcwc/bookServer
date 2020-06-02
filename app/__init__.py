from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config
from model.model import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app, supports_credentials=True)
    db.init_app(app)
    db.app = app
    db.create_all()

    register_blueprint(app)
    return app


def register_blueprint(app_context):
    from app.spider import spider  as spider_blueprint
    app_context.register_blueprint(spider_blueprint)
