from flask import request
from . import web
from app.forms.book import searchForm
from app.lib.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection
import json

@web.route('/book/search/')
def search():
    form = searchForm(request.args)
    book = BookCollection()
    if form.validate():
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
        # return yushu_book
