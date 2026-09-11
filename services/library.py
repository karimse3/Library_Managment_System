from models.book import Book
from models.member import Member
from enum import Enum

class BorrowResult(Enum):
    SUCCESS = "Success"
    BOOK_NOT_FOUND = "Book not found"
    MEMBER_NOT_FOUND = "Member not found"
    BOOK_NOT_AVAILABLE = "Book not available"
    LIMIT_REACHED = "Limit reached"

class ReturnResult(Enum):
    SUCCESS = "Success"
    BOOK_NOT_FOUND = "Book not found"
    MEMBER_NOT_FOUND = "Member not found"
    BOOK_ALREADY_AVAILABLE = "Book already available"
    BOOK_NOT_BORROWED_BY_MEMBER = "Member didn't borrow this book"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # Methods
    #===== Book Methods =====#
    def add_book(self, book: Book) -> bool:
        if book.book_id not in self.books:
            self.books[book.book_id] = book
            return True
        return False

    def remove_book(self, book_id: int) -> bool:
        book = self.find_book(book_id)
        if book and book.available:
            del self.books[book_id]
            return True
        return False



    def find_book(self, book_id: int) -> Book | None :

        return self.books.get(book_id)

    def get_books(self) -> list[Book]:
        return list(self.books.values())

    def display_books(self):
        for book in self.books.values():
            print(f"ID :{book.book_id}")
            print(f"Title :{book.title}")
            print(f"Author :{book.author}")
            print(f"ISBN :{book.isbn}")
            print(f"Availability Status :{"Available" if book.available else "Not available" }\n")

    def search_books(self, keyword: str) -> list[Book]:
        results = []
        keyword = keyword.strip().lower()
        for book in self.books.values() :
            books_match = keyword in book.title.strip().lower()
            author_match = keyword in book.author.strip().lower()
            if books_match or author_match :
                results.append(book)

        return results



    #===== Member Methods =====#
    def add_member(self, member: Member) -> bool:

        if member.member_id not in self.members:
            self.members[member.member_id] = member
            return True
        return False

    def remove_member(self, member_id: int) -> bool:
        member = self.find_member(member_id)
        if member and not member.borrowed_books:
            del self.members[member_id]
            return True
        return False

    def find_member(self, member_id: int) -> Member | None :
        return self.members.get(member_id)

    def get_members(self) -> list[Member]:
        return list(self.members.values())
    
    def display_members(self):
        for member in self.members:
            print(f"ID :{member.member_id}")
            print(f"Name :{member.name}")
            print(f"Email :{member.email}")
            print(f"Borrowed Books :{[book.title for book in member.borrowed_books
                                      if member.borrowed_books ]}\n")

    def search_members(self, keyword: str) -> list[Member]:
        results = []
        keyword = keyword.strip().lower()
        for member in self.members.values():
            names_match = keyword in member.name.strip().lower()
            emails_match = keyword in member.email.strip().lower()
            if names_match or emails_match:
                results.append(member)

        return results

    #===== Library Methods =====#
    def borrow_book(self, book_id: int, member_id: int) -> BorrowResult:
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if not book:
            return BorrowResult.BOOK_NOT_FOUND
        if not member:
            return BorrowResult.MEMBER_NOT_FOUND
        if not book.available :
            return BorrowResult.BOOK_NOT_AVAILABLE
        if len(member.borrowed_books) >= 4 :
            return BorrowResult.LIMIT_REACHED
        
        member.borrowed_books.append(book)
        book.available = False
        return BorrowResult.SUCCESS

    def return_book(self, book_id: int, member_id: int) -> ReturnResult:
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if not book:
            return ReturnResult.BOOK_NOT_FOUND
        if not member:
            return ReturnResult.MEMBER_NOT_FOUND
        if book.available :
            return ReturnResult.BOOK_ALREADY_AVAILABLE
        if book not in member.borrowed_books :
            return ReturnResult.BOOK_NOT_BORROWED_BY_MEMBER
        
        member.borrowed_books.remove(book)
        book.available = True
        return ReturnResult.SUCCESS