from . import web
from app.forms.auth import RegisterForm
from flask import request
from werkzeug.security import generate_password_hash
from app.model.user import User
from app.model.base import db



@web.route('/register',methods=['POST'])
def register():
    form = RegisterForm(data = request.json)
    if form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
            return "register"
            # user = User()
            # user.set_attrs(form.data)
            # db.session.add(user)
            # db.session.commit()
        return "register1"