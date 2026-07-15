from models.library import Library
from models.book import Book
from models.member import Member

def main():
    library = Library("SMIU")
    book1 = Book("Titanic", "Ashir")
    book2 = Book("Harry Poter", "Ghufran")
    member1 = library.registerMember("Ghufran")
    member2 = library.registerMember("Ashir")
    print(library.members[0].name, library.members[0].ID)

    library.addBook(book1)
    library.searchBook("Titanic")
    library.displayBooks()
    library.borrowBook(2,1)
    library.returnBook(2,1)

if __name__ == '__main__':
    main()
    