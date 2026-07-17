from models.member import Member
from exceptions import BookNotFoundError, MemberNotFoundError
class Library:
    next_member_id = 1
    next_book_id = 1
    def __init__(self, name):
        self.name = name
        self.members= []
        self.books = {} 

    def register_member(self, name):
        member_id = Library.next_member_id
        member = Member(name, member_id)
        self.members.append(member)
        print(f"{name} is now registered")
        Library.next_member_id +=1
        return member
    
    def add_book(self, book):
        book_id = Library.next_book_id
        self.books.update({ book_id: book})
        print(f"The {book.title} book is now available in the library.")
        Library.next_book_id += 1

    def remove_book(self, book_id):
            if book_id in self.books:
                self.books.pop(book_id)
                print(f"Book with ID {book_id} has been removed from the library.")
                return
            raise BookNotFoundError(book_id)        

    def search_book(self, book):
            if book in [b.title for b in self.books.values()]:
                print(f"{book} is available in the library.")
                return
            raise BookNotFoundError(book)

    def display_books(self):
        if self.books:
            print("Books available in the library:")
            for book_id, book in sorted(self.books.items()):
               print(f"{book_id} : {book.title} by {book.author}")
        else:
            print("No books available in the library.")

    def borrow_book(self, member_id, book_id):
                if book_id in self.books:
                    for member in self.members:
                        if member.ID == member_id:
                            book = self.books.pop(book_id)
                            member.borrowedBooks.append({book_id: book})
                            print(f"Book with ID {book_id} has been borrowed by member with ID {member_id}.")
                            return
                    raise MemberNotFoundError(member_id)
                raise BookNotFoundError(book_id)
            
    def return_book(self, member_id, book_id):
        for member in self.members:
              if member.ID == member_id:
                  for borrowed_book in member.borrowedBooks:
                      if book_id in borrowed_book:
                          book = borrowed_book.pop(book_id)
                          self.books[book_id] = book
                          print(f"Member with ID {member_id} returned Book with ID {book_id}.")
                          return
                  raise BookNotFoundError(book_id, f"Book with ID {book_id} is not borrowed by member with ID {member_id}.")
        raise MemberNotFoundError(member_id)
           