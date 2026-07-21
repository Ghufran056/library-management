class Book:
    def __init__(self, title, author, is_borrowed=False, borrowed_by =None):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by