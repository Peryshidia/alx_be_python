import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """
        Calculate the area of the shape.
        
        Returns:
            float: The area of the shape
            
        Raises:
            NotImplementedError: If the method is not implemented by a derived class
        """
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self) -> float:
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self) -> float:
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return math.pi * (self.radius ** 2)


# Example usage
if __name__ == "__main__":
    # Create instances of different shapes
    rectangle = Rectangle(5, 3)
    circle = Circle(4)
    
    # Calculate and print areas
    print(f"Rectangle area: {rectangle.area():.2f} square units")
    print(f"Circle area: {circle.area():.2f} square units")