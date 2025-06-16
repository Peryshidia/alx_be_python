class Book:
    """
    A class representing a book in the library system.
    """
    
    def __init__(self, title: str, author: str):
        """
        Initialize a new book.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False    
    def __str__(self) -> str:
        """Return a string representation of the book."""
        status = "Checked Out" if self._is_checked_out else "Available"
        return f"{self.title} by {self.author} - {status}"


class Library:
    """
    A class representing a library that manages a collection of books.
    """
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []
    
    def add_book(self, book: Book) -> None:
        """
        Add a book to the library.
        
        Args:
            book (Book): The book to add
        """
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")
    
    def check_out_book(self, title: str) -> bool:
        """
        Check out a book by its title.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if the book was successfully checked out, False otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower() and not book._is_checked_out:
                book._is_checked_out = True
                print(f"'{book.title}' has been checked out.")
                return True
        print(f"Book '{title}' is not available for checkout.")
        return False
    
    def return_book(self, title: str) -> bool:
        """
        Return a book to the library.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if the book was successfully returned, False otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower() and book._is_checked_out:
                book._is_checked_out = False
                print(f"'{book.title}' has been returned.")
                return True
        print(f"Book '{title}' was not checked out.")
        return False
    
    def list_available_books(self) -> None:
        """Display all available books in the library."""
        available_books = [book for book in self._books if not book._is_checked_out]
        
        if not available_books:
            print("No books are currently available.")
            return
            
        print("\nAvailable Books:")
        for book in available_books:
            print(f"- {book.title} by {book.author}")
    
    def list_all_books(self) -> None:
        """Display all books in the library and their status."""
        if not self._books:
            print("The library is empty.")
            return
            
        print("\nAll Books in Library:")
        for book in self._books:
            print(f"- {book}")