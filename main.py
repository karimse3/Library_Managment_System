from models.book import Book
from models.member import Member
from services.library import Library

library = Library()

book1 = Book(1, "Python Crash Course", "Robert C. Martin", "123")
book2 = Book(2, "Learning Python", "Eric Matthes", "456")
book3 = Book(3, "The Clean Coder", "Robert C. Martin", "122")


member1 = Member(1, "Karim", "karim@example.com")
member2 = Member(2, "Karim", "karim@example.com")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_member(member1)
library.add_member(member2)

library.borrow_book(1, 1)

library.search_book(keyword="pyth")