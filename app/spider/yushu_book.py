from app.lib.getHttp import HTTP
from flask import current_app

class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0,
        self.books = []

    def search_by_isbn(self):
        url = self.isbn_url
        result = HTTP.get(url)
        print(result)
        print(url)
        self.__fill_singer(result)

    def __fill_singer(self,data):
        if data:
            self.total = 1
            self.books.append(data)

    def search_by_keyword(self,keyword,page=1):
        url = self.keyword_url.format(keyword,current_app.config['PER_PAGE'],self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def __fill_collection(self,data):
        self.total = data['total']
        self.books = data['books']

    def calculate_start(self,page):
        return (page-1)*current_app.config['PER_PAGE']