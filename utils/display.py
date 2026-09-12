from models.book import Book
from models.member import Member

def display_book(book: Book):
    status = "Available" if book.available else "Not available"
    print(f"ID :{book.book_id}")
    print(f"Title :{book.title}")
    print(f"Author :{book.author}")
    print(f"ISBN :{book.isbn}")
    print(f"Availability Status :{status}")    

def display_member(member: Member):
    print(f"ID :{member.member_id}")
    print(f"Name :{member.name}")
    print(f"Email :{member.email}")
    print(f"Borrowed Books :{[book.title for book in member.borrowed_books]}\n")



