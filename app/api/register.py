from flask import make_response
from . import web
from app.validators.form import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum
from app.model.user import User
from app.libs.error_code import Success


@web.route('/register', methods=['POST'])
def register():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL.value: __register_user_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(
        form.nickname.data,
        form.account.data,
        form.password.data
    )