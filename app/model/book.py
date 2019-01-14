import json
from sqlalchemy import Column, String, Integer
from app.model.base import Base, db


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(60), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def keys(self):
        return ['id', 'title', 'author', 'binding', 'publisher', 'price', 'pages', 'pubdate', 'isbn', 'summary', 'image']

    def add_to_current_upload(book):
        book_detail = json.loads(book).get('book')
        for book_list in book_detail:
            with db.auto_commit():
                books = Book()
                books.title = book_list['title']
                books.author = book_list['author']
                books.binding = book_list['binding']
                books.publisher = book_list['publisher']
                books.price = book_list['price']
                books.pages = book_list['pages']
                books.pubdate = book_list['pubdate']
                books.isbn = book_list['isbn']
                books.summary = book_list['summary']
                books.image = book_list['image']
                db.session.add(books)

