class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("Library is empty.")
            return
        print("Books available in the library:")
        for book in self.books:
            print(book)

def main():
    library = Library()

    # Adding some books to the library
    book1 = Book("1984", "George Orwell", "9780451524935")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book4 = Book("Harry Potter", "J.K. Rowling", "97807475327433")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)
            print("Book added successfully.")

        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            for book in library.books:
                if title.lower() == book.title.lower():
                    library.remove_book(book)
                    print("Book removed successfully.")
                    break
            else:
                print("Book not found.")

        elif choice == '3':
            title = input("Enter the title of the book to search: ")
            library.search_book(title)

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
