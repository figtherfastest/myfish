from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from app.lib.error_code import AuthFailed
from collections import namedtuple

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type'])


# 验证是否登录，那就是判断token是否过期
@auth.verify_password
def verify_password(token):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config('SECRET_KEY'))
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token in expired', error_code=1003)

    uid =data['uid']
    ac_type = data['type']

    return User(uid, ac_type)