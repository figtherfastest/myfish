from flask import current_app, jsonify
from . import web
from app.validators.form import ClientForm
from app.lib.enum import ClientTypeEnmu
from app.model.user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@web.route('/token', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnmu.USER_EMAIL: User.verify
    }
    identity = promise[ClientTypeEnmu(form.type.data)](
        form.account.data,
        form.password.data
    )
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = genert_auth_token(
        identity['uid'],
        form.type.data,
        None,
        expiration
    )
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t)

def genert_auth_token(uid, ac_type,scoped=None,expiration=7200):
    # 生成令牌
    s = Serializer(current_app.config['SECRET_KEY'], expiration=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value
    })
