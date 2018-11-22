from flask import request
from . import web
from app.forms.book import searchForm

@web.route('/book/search/')
def search():
    form = searchForm(request.form)
    print(form)
    if form.validate():
        return 'hello word'
