# City Library System

The **City Library System** is a simple console-based application designed to manage book lending and returning in a library setting. It allows users to add new books, search for existing books, lend books to patrons, and return books that have been previously borrowed.

## Features

- Add new books to the library
- Search for books by title
- Lend books to users (if available)
- Return borrowed books
- Prepopulate the library with a set of classic literature titles

## Classes

### `Book`
Represents a book in the library.

- **Attributes:**
  - `title`: The title of the book.
  - `author`: The author of the book.
  - `is_available`: A boolean indicating whether the book is currently available for lending.

- **Methods:**
  - `check_out()`: Checks out the book, making it unavailable for borrowing.
  - `return_book()`: Returns the book, making it available for borrowing.

### `Library`
Represents the library which contains a collection of books.

- **Attributes:**
  - `books`: A list that stores all the books in the library.
  - `book_index`: A dictionary that maps book titles to their corresponding `Book` objects for quick access.

- **Methods:**
  - `add_book(book)`: Adds a new book to the library.
  - `search_book(title)`: Searches for a book by title. Returns the book object if found; otherwise `None`.
  - `lend_book(title)`: Lends a book to the user if it is available.
  - `return_book(title)`: Returns a borrowed book to the library.
  - `prepopulate_books()`: Fills the library with a set of predefined books.

## Usage

1. Clone or download the repository to your local machine.
2. Open the terminal and navigate to the project directory.
3. Run the application using Python:

   ```bash
   python main.py
