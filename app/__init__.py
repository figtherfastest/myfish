from flask import Flask as _Flask
from flask_cors import *
from app.model.base import db
from flask.json import JSONEncoder as _JSONEncoder
from datetime import date
from app.libs.error_code import ServerError


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
    from app.api import web
    app.register_blueprint(web)


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
