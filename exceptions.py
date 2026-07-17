class BookNotFoundError(Exception):
    def __init__(self, Book_id, message="Book not found in the library."):
        self.Book_id = Book_id
        super().__init__(message)

class MemberNotFoundError(Exception):
    def __init__(self, Member_id):
        self.Member_id = Member_id
        super().__init__(f"Member with ID {Member_id} is not registered in the library.")