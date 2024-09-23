# library.py

from book import Book

class Library:
    def __init__(self):
        self.books = []
        self.book_index = {}

    def add_book(self, book):
        self.books.append(book)
        self.book_index[book.title] = book

    def search_book(self, title):
        return self.book_index.get(title, None)

    def lend_book(self, title):
        book = self.search_book(title)
        if book and book.check_out():
            return f"The book '{title}' has been lent out."
        elif book:
            return f"The book '{title}' is currently unavailable."
        else:
            return f"The book '{title}' does not exist in the library."

    def return_book(self, title):
        book = self.search_book(title)
        if book:
            book.return_book()
            return f"The book '{title}' has been returned."
        else:
            return f"The book '{title}' does not exist in the library."

    def prepopulate_books(self):
        prepopulated_books = [
            Book("To Kill a Mockingbird", "Harper Lee"),
            Book("1984", "George Orwell"),
            Book("Pride and Prejudice", "Jane Austen"),
            Book("The Great Gatsby", "F. Scott Fitzgerald"),
            Book("Moby-Dick", "Herman Melville")
        ]
        for book in prepopulated_books:
            self.add_book(book)
