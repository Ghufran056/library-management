from pathlib import Path
import json
from models.member import Member
from models.book import Book
from exceptions import BookNotFoundError, MemberNotFoundError
class Library:
    next_member_id = 1
    next_book_id = 1

    def __init__(self, name):
        self.name = name
        self.members= []
        self.books = {} 
    
        self.file_path = Path("library_data.json")

    def save_library_data(self):
        library_data = {
            "name" : self.name,
            "members" : [member.__dict__ for member in self.members],
            "books" : {k: book.__dict__ for k, book in self.books.items()}
        }

        with open("library_data.json", "w") as file:
             json.dump(library_data, file, indent=4)
        print("Library data saved to library.json")

    def load_library_data(self):
        if not self.file_path.exists():
            return
        try:
            with open("library_data.json", "r") as file:
                data = json.load(file)
                self.name = data["name"]   
                self.members = [Member(**member) for member in data["members"]]
                self.books = {int(k): Book(**book) for k, book in data["books"].items()}
                if self.members:
                     Library.next_member_id  = max(member.ID for member in self.members) + 1
                if self.books:
                     Library.next_book_id = max(self.books.keys()) + 1
        except FileNotFoundError:
             print("No saved library data found. Starting with an empty library.")
             
    
    def register_member(self, name):
        member_id = Library.next_member_id
        member = Member(name, member_id)
        self.members.append(member)
        print(f"{name} is now registered")
        Library.next_member_id +=1
        self.save_library_data()
        return member
    
    def add_book(self, book):
        book_id = Library.next_book_id
        self.books.update({ book_id: book})
        Library.next_book_id += 1
        self.save_library_data()
        print(f"The {book.title} book is now available in the library.")
        

    def remove_book(self, book_id):
            if book_id in self.books:
                self.books.pop(book_id)
                self.save_library_data()
                print(f"Book with ID {book_id} has been removed from the library.")
                return
            raise BookNotFoundError(book_id)        

    def search_book(self, book):
            for b in self.books.values():
                if book in b.title:
                    if not b.is_borrowed:
                        print(f"{book} is available in the library.")
                        return
            raise BookNotFoundError(book)

    def display_books(self):
        count = 0
        print("Books available in the library:")
        for book_id, book in sorted(self.books.items()):
            if not book.is_borrowed:
                print(f"{book_id} : {book.title} by {book.author}")
                count +=1
        if count == 0:
            print("No books available in the library.")

    def borrow_book(self, member_id, book_id):
                if book_id in self.books:
                    if not self.books[book_id].is_borrowed:
                        for member in self.members:
                            if member.ID == member_id:
                                self.books[book_id].is_borrowed = True
                                self.books[book_id].borrowed_by = member_id
                                member.borrowedBooks.append(book_id)
                                self.save_library_data()
                                print(f"Book with ID {book_id} has been borrowed by member with ID {member_id}.")
                                return
                        raise MemberNotFoundError(member_id)
                    raise BookNotFoundError(book_id, f"Book already borrowed by other member")
                raise BookNotFoundError(book_id)
            
    def return_book(self, member_id, book_id):
        for member in self.members:
              if member.ID == member_id:
                    if book_id in member.borrowedBooks:
                        member.borrowedBooks.remove(book_id)
                        self.books[book_id].is_borrowed = False
                        self.books[book_id].borrowed_by = None
                        self.save_library_data()
                        print(f"Member with ID {member_id} returned Book with ID {book_id}.")
                        return
                    raise BookNotFoundError(book_id, f"Book with ID {book_id} is not borrowed by member with ID {member_id}.")
        raise MemberNotFoundError(member_id)
           

    