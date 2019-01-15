from flask import g
from app.api import web
from app.libs.token_auth import auth
from app.model.base import db
from app.model.wish import Wishes
from app.libs.error_code import Success
from app.validators.form import addToWish


@web.route('/saveWish', methods=['POST'])
@auth.login_required
def save_to_wish():
    form = addToWish().validate_for_api()
    print(g.user)
    with db.auto_commit():
        wish = Wishes()
        wish.wishIsbn = form.isbn.data
        wish.uid = g.user.id
        db.session.add(wish)
    return Success()