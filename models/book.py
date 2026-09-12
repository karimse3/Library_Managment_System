class Book:
    """Represent a book in the library.

    Attributes:
        book_id: Unique identifier of the book.
        title: Title of the book.
        author: Author of the book.
        isbn: International Standard Book Number.
        available: Whether the book is currently available.
    """
    def __init__(self, book_id: int, title: str, author: str, isbn: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available: bool = True 