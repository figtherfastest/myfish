from flask import g
from app.api import web
from app.libs.token_auth import auth
from app.spider.yushu_book import YuShuBook
from app.model.base import db
from app.model.wish import Wish
from app.libs.error_code import Success


@web.route('/getWish', methods=['GET'])
@auth.login_required
def get_wishes():
    pass


@web.route('/saveWish/<isbn>', methods=['POST'])
@auth.login_required
def save_to_wish(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    with db.auto_commit():
        wish = Wish()
        wish.wishIsbn = yushu_book.books[0]['isbn']
        wish.id = g.user.id
        db.session.add(wish)
    return Success()