from dataclasses import dataclass

class ParamTypeError(Exception):
    def __init__(self, param):
        self.param = type(param)
        Exception.__init__(self, f"Параметр не соответствует типу данных {type(param)}")


@dataclass
class Book:
    book_id = None
    author: str
    year: int
    pages: int
    price: int

    def __post_init__(self):
        if type(self.pages) != type(0) or type(self.year) != type(0) or type(self.price) != type(0):
            raise ParamTypeError(0)

        if type(self.author) != type(""):
            raise ParamTypeError("")

    def __str__(self):
        return f"ID:{self.book_id} \nAuthor:{self.author} \nYear:{self.year} \nPages:{self.pages} \nPrice:{self.price}"

    def price_equal(self, book):
        if self.price == book.price:
            print("ОДИНАКОВО")
        elif self.price > book.price:
            print("ДОРОЖЕ")
        elif self.price < book.price:
            print("Дешевле")


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        book.book_id = len(self.books) + 1
        self.books.append(book)

    def get_book_info(self, find):
        for book in self.books:
            if book.book_id == find:
                print(book)
                break
        else:
            print("Not found")

    def find_author(self, *args):
        num = 0
        for author in args:
            for book in self.books:
                if book.author == author:
                    print(book)
                    num += 1

        if num == 0:
            print("Not found")

    def __str__(self):
        return str(self.books)
