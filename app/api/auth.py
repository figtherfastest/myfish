from . import web
from app.validators.form import RegisterForm
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


