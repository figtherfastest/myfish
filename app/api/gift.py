from flask import g
from app.libs.token_auth import auth
from app.api import web
from app.spider.yushu_book import YuShuBook
from app.model.base import db
from app.model.gift import Gift
from app.libs.error_code import Success
from app.model.user import User
from app.libs.error_code import NotFound


# 加入赠送清单  条件就是既不能在心愿清单，也不能在赠送清单
@web.route('/saveGift/<isbn>', methods=['POST'])
@auth.login_required
def save_to_gifts(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    user_id = g.user.id
    if User.can_save_to_list(isbn, user_id):
        with db.auto_commit():
            gift = Gift()
            gift.id = user_id
            gift.bookIsbn = yushu_book.books[0]['isbn']
            db.session.add(gift)
        return Success()
    else:
        raise NotFound(msg="当前书籍已经加入心愿清单，请不要重复加入")
