from flask import current_app, jsonify
from . import web
from app.validators.form import ClientForm
from app.libs.enums import ClientTypeEnum
from app.model.user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@web.route('/login', methods=['POST'])
def login():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL.value: User.verify
    }
    identity = promise[form.type.data](
        form.account.data,
        form.password.data
    )
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(
        identity['id'],
        form.type.data,
        identity['scope'],
        expiration
    )
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(id, ac_type, scope=None,expiration=7200):
    # 生成令牌
    print(expiration)
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'id': id,
        'type': ac_type,
        'scope': scope
    })
