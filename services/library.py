from models.book import Book
from models.member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Methods
    #===== Book Methods =====#
    def add_book(self, book: Book) -> bool:
        books_ids = [book.book_id for book in self.books ]

        if book.book_id not in books_ids:
            self.books.append(book)
            return True
        return False

    def remove_book(self, book_id: int) -> bool:
        book = self.find_book(book_id)
        if book and book.available:
            self.books.remove(book)
            return True
        return False



    def find_book(self, book_id: int) -> Book | None :
        for book in self.books:
            if book.book_id == book_id:
                return book

        return None

    def display_books(self):
        for book in self.books:
            print(f"ID :{book.book_id}")
            print(f"Title :{book.title}")
            print(f"Author :{book.author}")
            print(f"ISBN :{book.isbn}")
            print(f"Availability Status :{"Available" if book.available else "Not available" }\n")

    def search_book(self, keyword):
        index = 1
        keyword = keyword.strip().lower()
        for book in self.books :
            books_match = keyword in book.title.strip().lower()
            author_match = keyword in book.author.strip().lower()
            if books_match or author_match :
                print(f"{index}. {book.title} -- {book.author}")
                index += 1
        if index == 1 :
            print("No books found")


    #===== Member Methods =====#
    def add_member(self, member: Member) -> bool:
        members_ids = [member.member_id for member in self.members ]

        if member.member_id not in members_ids:
            self.members.append(member)
            return True
        return False

    def remove_member(self, member_id: int) -> bool:
        member = self.find_member(member_id)
        if member and not member.borrowed_books:
            self.members.remove(member)
            return True
        return False

    def find_member(self, member_id: int) -> Member | None :
        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    def display_members(self):
        for member in self.members:
            print(f"ID :{member.member_id}")
            print(f"Name :{member.name}")
            print(f"Email :{member.email}")
            print(f"Borrowed Books :{[book.title for book in member.borrowed_books
                                      if member.borrowed_books ]}\n")

    def search_member(self, keyword):
        index = 1
        keyword = keyword.strip().lower()
        for member in self.members:
            names_match = keyword in member.name.strip().lower()
            emails_match = keyword in member.email.strip().lower()
            if names_match or emails_match:
                print(f"{index}. {member.name} -- {member.email} -- Borrowed : {len(member.borrowed_books)}")
                index +=1

        if index == 1:
            print("No members found")

    #===== Library Methods =====#
    def borrow_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        if book and member :
            if book.available and len(member.borrowed_books) < 4:
                member.borrowed_books.append(book)
                book.available = False
                print("Book borrowed successfully")
            elif not book.available :
                print("The book is not available")
            elif len(member.borrowed_books) > 4 :
                print("This member has borrowed too many books")
        elif not book:
            print("Book not found")
        elif not member:
            print("Member not found")

    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        if book and member :
            if not book.available and book in member.borrowed_books:
                member.borrowed_books.remove(book)
                book.available = True
                print("Book returned successfully")
            elif book.available :
                print("The book is already available")
            elif book not in member.borrowed_books :
                print("This member didn't borrow this book")
        elif not book:
            print("Book not found")
        elif not member:
            print("Member not found")