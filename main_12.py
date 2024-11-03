from classes_12 import Book, Library

book1 = Book("Ayder", 2001, 400, 2500)
book2 = Book("dff", 2322, 23, 2500)

library1 = Library()
library1.add_book(book1)
library1.add_book(book2)
library1.get_book_info(1)
library1.get_book_info(2)
book2.price_equal(book1)
print()

print(library1)

