from . import web
from app.forms.auth import RegisterForm
from flask import request
from werkzeug.security import generate_password_hash
from app.model.user import User
from app.model.base import db



@web.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    print(request.form)
    print(form.validate())
    if request.method == 'POST' and form.validate():
        # user = User()
        # user.set_attrs(form.data)
        # db.session.add(user)
        # db.session.commit()
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
    return "register"