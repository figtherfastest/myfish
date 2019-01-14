from flask import g
from app.api import web
from app.libs.token_auth import auth
from app.model.base import db
from app.model.wish import Wish
from app.libs.error_code import Success


@web.route('/saveWish', methods=['POST'])
@auth.login_required
def save_to_wish():
    with db.auto_commit():
        wish = Wish()
        wish.wishIsbn = isbn
        wish.uid = g.user.id
        db.session.add(wish)
    return Success()