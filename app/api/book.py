from flask import request
from . import web
from app.validators.form import searchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection
from app.view_models.book import BookViewModel
from app.libs.token_auth import auth
import json


@web.route('/book/search', methods=['GET'])
@auth.login_required
def book_search():
    form = searchForm().validate_for_api()
    book = BookCollection()

    q = form.q.data
    page = form.page.data
    isbn_or_key = is_isbn_or_key(q)

    yushu_book = YuShuBook()
    if isbn_or_key == 'isbn':
        yushu_book.search_by_isbn(q)
    else:
        yushu_book.search_by_keyword(q, page)
    book.fill(yushu_book, q)
    return json.dumps(book, default=lambda o: o.__dict__)


@web.route('/book/detail/<isbn>', methods=['GET'])
@auth.login_required
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.books[0])
    return json.dumps(book, default=lambda o: o.__dict__)



