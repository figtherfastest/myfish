from . import web
from app.lib.token_auth import auth

@web.route('/my/gift')
@auth.login_required()
def my_gifts():
    pass

