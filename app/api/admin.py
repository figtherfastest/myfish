from . import web
from app.libs.token_auth import auth


@web.route('/userList', methods=['GET'])
@auth.login_required
def getUserList():
    pass