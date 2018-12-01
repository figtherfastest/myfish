
class BookViewModel:
    def __init__(self, book):
        self.title = book['title'],
        self.author = '、'.join(book['author']),
        self.publisher = book['publisher'],
        self.image = book['image'],
        self.price = book['price'],
        self.summary = book['summary'],
        self.pages = book['pages'],
        self.isbn = book['isbn'],
        self.pubdate = book['pubdate'],
        self.binding = book['binding']

    def intro(self):
        intro = filter(lambda x:True if x else False,[
            self.author, self.publisher, self.price
        ])

        return '/'.join(intro)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.book = []
        self.keyword = ""

    def fill(self, yushu_book,keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.book = [BookViewModel(book) for book in yushu_book.books]