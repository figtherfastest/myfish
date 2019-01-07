from . import web
from app.validators.form import ClientForm
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.validators.form import resetPsd
from app.model.user import User


@web.route('/resetPassword', methods=['POST'])
def resetPassword():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL.value:__reset_user_by_email
    }
    promise[form.type.data]()
    return Success()


def __reset_user_by_email():
    form = resetPsd().validate_for_api()
    user = User.query.filter_by(email=form.account.data).first_or_404()
    User.reset_by_email(user, form.password.data)
