class Library:
    next_member_id = 1
    next_book_id = 1
    def __init__(self, name):
        self.name = name
        self.members= []
        self.books = [] 

    def registerMember(self, name):
        member_id = Library.next_member_id
        member = Member(name, member_id)
        self.members.append(member)
        print(f"{name} is now registered")
        Library.next_member_id +=1
        return member
    
    def addBook(self, book):
        book_id = Library.next_book_id
        self.books.append({ book_id: book})
        print(f"The {book.title} book is now available in the library.")
        Library.next_book_id += 1

    def removeBook(self, book_id):
        for book in self.books:
            if book_id in book:
                self.books.remove(book)
                print(f"Book with ID {book_id} has been removed from the library.")
                return
            else:
                print(f"Book with ID:{book_id} is not available in the library.")

    def searchBook(self, book):
        for Book in self.books:
            if book in [b.title for b in Book.values()]:
                print(f"{book} is available in the library.")
                return
            else:
                print(f"{book} is not available in the library.")

    def displayBooks(self):
        if self.books:
            print("Books available in the library:")
            for book in self.books:
                for k, obj in book.items():
                    print(f"{k} : {(obj.title)}")
        else:
            print("No books available in the library.")

    def borrowBook(self, member_id, book_id):
        if member_id in [member.ID for member in self.members]:
            for book in self.books:
                if book_id in book:
                    self.members[member_id - 1].borrowedBooks.append(book)
                    self.books.remove(book)
                    print(f"Book with ID {book_id} has been borrowed by member with ID {member_id}.")
                    return
                else:
                    print(f"Book with ID {book_id} is not available in the library.")
        else:
            print(f"Member with ID {member_id} is not registered in the library.")

    def returnBook(self, member_id, book_id):
        if member_id in [member.ID for member in self.members]:
            for book in self.members[member_id - 1].borrowedBooks:
                if book_id in book:
                    return_book_index = self.members[member_id - 1].borrowedBooks.index(book)
                    return_book = self.members[member_id - 1].borrowedBooks.pop(return_book_index)

                    self.books.append(return_book)
                    print(f"member with ID: {member_id} returned Book with ID: {book_id}")
                else:
                    print("Book not found")

        else:
            print("member is not registered")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.ID = member_id
        self.borrowedBooks = []

    def borrowedBooks(self):
        if self.borrowedBooks:
            print(f"{self.name} has borrowed the following books:")
            for i, book in enumerate(self.borrowedBooks, start=1):
                print(f"{i}. {book}")
        else:
            print(f"{self.name} has not borrowed any books.")

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
main()
    