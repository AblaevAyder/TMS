from classes_12 import Book, Library

book1 = Book("Ayder", 2001, 400, 2500)
book2 = Book("dff", 2322, 23, 2322)

library1 = Library()
library1.add_book(book1)
library1.add_book(book2)
library1.get_book_info(1)
print()

print(library1)

