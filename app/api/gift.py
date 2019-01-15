from flask import g
from app.libs.token_auth import auth
from app.api import web
from app.spider.yushu_book import YuShuBook
from app.model.base import db
from app.model.gift import Gift
from app.libs.error_code import Success


@web.route('/saveGift/<isbn>', methods=['POST'])
@auth.login_required
def save_to_gifts(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    with db.auto_commit():
        gift = Gift()
        gift.id = g.user.id
        gift.bookIsbn = yushu_book.books[0]['isbn']
        db.session.add(gift)
    return Success()
