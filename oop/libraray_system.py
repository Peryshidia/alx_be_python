class Book:
    def __init__(self, title: str, author: str):
        """
        Initialize a Book instance with title and author.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self) -> str:
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The size of the ebook file in kilobytes
        """
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self) -> str:
        """Return a string representation of the ebook."""
        return f"{super().__str__()} (E-Book, {self.file_size}KB)"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages in the book
        """
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self) -> str:
        """Return a string representation of the print book."""
        return f"{super().__str__()} (Print Book, {self.page_count} pages)"


class Library:
    def __init__(self):
        """Initialize an empty library."""
        self.books = []
    
    def add_book(self, book: Book) -> None:
        """
        Add a book to the library.
        
        Args:
            book (Book): A Book, EBook, or PrintBook instance to add to the library
        """
        self.books.append(book)
    
    def list_books(self) -> None:
        """Print details of all books in the library."""
        if not self.books:
            print("The library is empty.")
            return
        
        print("\nLibrary Catalog:")
        print("-" * 50)
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        print("-" * 50)