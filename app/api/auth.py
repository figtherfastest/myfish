from . import web
from app.forms.auth import RegisterForm
from flask import request
from app.model.user import User
from app.model.base import db
from app.lib.error_code import Success



@web.route('/register',methods=['POST'])
def register():
    form = RegisterForm().validate_for_api()
    with db.auto_commit():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
    return Success()
    # form = RegisterForm(data = request.json)
    # if form.validate():
    #     with db.auto_commit():
    #         user = User()
    #         user.set_attrs(form.data)
    #         db.session.add(user)
    #         # user = User()
    #         # user.set_attrs(form.data)
    #         # db.session.add(user)
    #         # db.session.commit()
    #     return "register1"

