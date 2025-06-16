class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a Book instance with title, author, and publication year.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor that prints a message when the book object is deleted."""
        print(f"Deleting {self.title}")
    
    def __str__(self) -> str:
        """
        Return a string representation of the book.
        
        Returns:
            str: A formatted string containing book details
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self) -> str:
        """
        Return the official string representation of the book.
        
        Returns:
            str: A string that can be used to recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"