from flask import jsonify
from . import web
from app.validators.form import searchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection
from app.view_models.book import BookViewModel
from app.libs.token_auth import auth
from app.model.book import Book
import json
from app.libs.error_code import Success


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
    book_detail = json.dumps(book, default=lambda o: o.__dict__)
    Book.add_to_current_upload(book_detail)
    return book_detail


@web.route('/book/detail/<isbn>', methods=['GET'])
@auth.login_required
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.books[0])
    return json.dumps(book, default=lambda o: o.__dict__)


@web.route('/book/getCurrent', methods=['GET'])
@auth.login_required
def get_current_upload():
    book_all = Book.query.filter_by().all()
    status_code = Success.__dict__
    book_status = {
        'status': {
            'code': status_code['code'],
            'msg': status_code['msg'],
            'error_code': status_code['error_code']
        },
        'book': book_all
    }
    return jsonify(book_status)