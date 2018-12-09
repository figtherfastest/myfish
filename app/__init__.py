from flask import Flask
from flask_cors import CORS
from app.model.base import db

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("app.secure")
    app.config.from_object("app.setting")
    register_blueprint(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)