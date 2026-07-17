from models.library import Library
from models.book import Book
from models.member import Member
from exceptions import BookNotFoundError, MemberNotFoundError

def main():
    library = Library("SMIU")
    book1 = Book("Titanic", "Ashir")
    book2 = Book("Harry Poter", "Ghufran")
    member1 = library.register_member("Ghufran")
    member2 = library.register_member("Ashir")
    print(library.members[0].name, library.members[0].ID)
    try:
        library.add_book(book1)
        library.add_book(book2)
        library.search_book("Titanic")
        library.display_books()
        library.borrow_book(2,1)
        library.return_book(2,1)
        library.display_books()
    except (BookNotFoundError, MemberNotFoundError) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
    