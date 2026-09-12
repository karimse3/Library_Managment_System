from models.book import Book
from models.member import Member
from services.library import Library
from utils.display import display_book, display_member
from utils.input_helpers import (
    ask_for_choice,
    ask_for_integer,
    ask_for_text,
    ask_for_email,
)


def main():
    library = Library()

#================================
#==== Books Managment System ====
#================================

    def books_management():
     while True :
        print("""========== BOOK MANAGEMENT ==========

1. Add Book
2. Remove Book
3. Search Book
4. Display Books
5. Back
""")
        choice = ask_for_choice("Choose an option :", 1, 5)
        if choice == 1:
            book = Book(
                ask_for_integer("Enter the ID :"),
                ask_for_text("Enter the title :"),
                ask_for_text("Enter the author :"),
                ask_for_text("Enter the isbn :"),
                            )
            result = library.add_book(book)
            if result:
                print("Book added successfully")
            else :
                print("This book already exists")
        elif choice == 2:
            book_id = ask_for_integer("Enter the ID :")
            result = library.remove_book(book_id)
            print(result.value)
        elif choice == 3:
            book_id = ask_for_integer("Enter the ID :")
            book = library.find_book(book_id)
            if book :
                display_book(book)
            else:
                print("Book not found")
        elif choice == 4:
            books = library.get_books()
            if books :
                for book in books:
                    display_book(book)
            else:
                print("No book to display")
        elif choice == 5:
            break
        else:
            print("No option")


#================================
#=== Student Managment System ===
#================================

    def members_management():
     while True :
        print("""========== MEMBER MANAGEMENT ==========

1. Add Member
2. Remove Member
3. Search Member
4. Display Members
5. Back
""")
        choice = ask_for_choice("Choose an option :", 1, 5)
        if choice == 1:
            member = Member(
                ask_for_integer("Enter the ID :"),
                ask_for_text("Enter the name :"),
                ask_for_email("Enter the email :"),
                            )
            result = library.add_member(member)
            if result:
                print("Member added successfully")
            else :
                print("This member already exists")
        elif choice == 2:
            member_id = ask_for_integer("Enter the ID :")
            result = library.remove_member(member_id)
            print(result.value)
        elif choice == 3:
            member_id = ask_for_integer("Enter the ID :")
            member = library.find_member(member_id)
            if member :
                display_member(member)
            else:
                print("Member not found")
        elif choice == 4:
            members = library.get_members()
            if members:
                for member in members:
                    display_member(member)
            else :
                print("No members to display")
        elif choice == 5:
            break
        else:
            print("No option")


#======================
#=== Search Section ===
#======================

    def search():
         
     while True :
        print("""========== SEARCH ==========

1. Search Book
2. Search Member
3. Back
""")
        choice = ask_for_choice("Choose an option :", 1, 3)
        if choice == 1:
            keyword  = str(input("Enter a title or author name: "))
            result = library.search_books(keyword)
            if result :
                for index, book in enumerate(result, start=1):
                    print(f"{index}. {book.title} -- {book.author}")
            else :
                print("No books found")

        elif choice == 2:
            keyword  = str(input("Enter a name or email: "))
            result = library.search_members(keyword)
            if result :
                for index, member in enumerate(result, start=1):
                    print(f"{index}. {member.name} -- {member.email}")
            else :
                print("No members found")
        elif choice == 3:
            break
        else:
            print("No option")


    while True :
        print("""╔════════════════════════════════════╗
║     LIBRARY MANAGEMENT SYSTEM      ║
╚════════════════════════════════════╝

1. Books
2. Members
3. Borrow book
4. Return book
5. Search
6. Exit """)
        choice = ask_for_choice("Choose an option :", 1, 6)
        if choice == 1:
            books_management()
        elif choice == 2:
            members_management()
        elif choice == 3:
            book_id = ask_for_integer("Enter book ID: ")
            member_id = ask_for_integer("Enter member ID: ")
            result = library.borrow_book(book_id, member_id)
            print(result.value)
        elif choice == 4:
            book_id = ask_for_integer("Enter book ID: ")
            member_id = ask_for_integer("Enter member ID: ")
            result = library.return_book(book_id, member_id)
            print(result.value)
        elif choice == 5:
            search()
        elif choice == 6:
            break
        else :
            print("No option")
    
    

if __name__ == "__main__":
    main()