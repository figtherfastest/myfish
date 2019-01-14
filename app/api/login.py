from flask import current_app, jsonify, make_response
from . import web
from app.validators.form import ClientForm
from app.libs.enums import ClientTypeEnum
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.libs.error_code import Success
from app.libs.responce import make_resp
from app.model.user import User


@web.route('/login', methods=['POST'])
def login():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL.value: User.verify
    }
    account = form.account.data
    password = form.password.data
    identity = promise[form.type.data](account, password)
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(
        identity['id'],
        form.type.data,
        identity['scope'],
        expiration
    )
    result_token = token.decode('ascii')
    return make_resp(Success, 'token', result_token)


def generate_auth_token(id, ac_type, scope=None, expiration=7200):
    # 生成令牌
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'id': id,
        'type': ac_type,
        'scope': scope
    })

