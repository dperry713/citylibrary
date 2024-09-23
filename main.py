# main.py

from library import Library

def display_menu():
    print("\nCity Library System")
    print("1. Add a new book")
    print("2. Search for a book by title")
    print("3. Lend a book")
    print("4. Return a book")
    print("5. Exit")

def main():
    library = Library()
    library.prepopulate_books()  # Prepopulate the library with some books

    while True:
        display_menu()
        choice = input("Choose an action: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(title, author)
            library.add_book(book)
            print(f"Book '{title}' by {author} added to the library.")

        elif choice == '2':
            title = input("Enter book title to search: ")
            book = library.search_book(title)
            if book:
                status = "available" if book.is_available else "unavailable"
                print(f"Book '{title}' by {book.author} is {status}.")
            else:
                print(f"Book '{title}' not found in the library.")

        elif choice == '3':
            title = input("Enter book title to lend: ")
            print(library.lend_book(title))

        elif choice == '4':
            title = input("Enter book title to return: ")
            print(library.return_book(title))

        elif choice == '5':
            print("Exiting the City Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
