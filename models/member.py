from book import Book

class Member:
    """Represent a member in the library.

    Attributes:
        member_id: Unique identifier of the member.
        name: Name of the member.
        email: Email address of the member.
        borrowed_books: Books that the member has borrowed
    """
    def __init__(self, member_id: int, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books: list[Book] = []
