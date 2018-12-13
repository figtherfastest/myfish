from . import web
from app.validators.form import RegisterForm, UserEmailForm
from app.model.user import User
from app.model.base import db
from app.lib.error_code import Success
from app.lib.enum import ClientTypeEnmu


@web.route('/register',methods=['POST'])
def register():
    form = RegisterForm().validate_for_api()
    promise = {
        ClientTypeEnmu.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm.validate_for_api()
    with db.auto_commit():
        user = User()
        user.nickname = form.nickname.data
        user.email = form.account.data
        user.password = form.password.data
        db.session.add(user)


# @web.route('/register',methods=['POST'])
# def register():
#     form = RegisterForm().validate_for_api()
#     with db.auto_commit():
#         user = User()
#         user.set_attrs(form.data)
#         db.session.add(user)
#     return Success()
