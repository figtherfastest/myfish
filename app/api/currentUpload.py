from . import web
from app.libs.token_auth import auth


@web.route('/currentUpload', methods=['POST'])
@auth.login_required
def current_upload():
    pass