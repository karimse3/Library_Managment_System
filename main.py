from models.book import Book
from models.member import Member
from services.library import Library

library = Library()

book1 = Book(1, "Python Crash Course", "Robert C. Martin", "123")
book2 = Book(2, "Learning Python", "Eric Matthes", "456")
book3 = Book(1, "The Clean Coder", "Robert C. Martin", "122")


member1 = Member(1, "Karim", "karim@example.com")
member2 = Member(2, "Karim", "karim@example.com")

if library.add_book(book1):
    print("Book added successfully")
else:
    print("This book already exists")

if library.add_book(book2):
    print("Book added successfully")
else:
    print("This book already exists")

if library.add_book(book3):
    print("Book added successfully")
else:
    print("This book already exists")

library.add_member(member1)
library.add_member(member2)

library.borrow_book(1, 1)

library.search_book(keyword="pyth")
library.search_member(keyword="kar")