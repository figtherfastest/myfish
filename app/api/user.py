from flask import jsonify, g
from app.model.user import User
from app.libs.token_auth import auth
from . import web


@web.route('/getUser', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.id
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@web.route('/getUsers', methods=['GET'])
@auth.login_required
def get_users():
    pass