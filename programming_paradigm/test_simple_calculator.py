class SimpleCalculator:
    """
    A simple calculator class that provides basic arithmetic operations.
    """
    
    def add(self, x: float, y: float) -> float:
        """
        Add two numbers.
        
        Args:
            x: First number
            y: Second number
            
        Returns:
            float: Sum of x and y
        """
        return x + y
    
    def subtract(self, x: float, y: float) -> float:
        """
        Subtract y from x.
        
        Args:
            x: First number
            y: Second number
            
        Returns:
            float: Difference between x and y
        """
        return x - y
    
    def multiply(self, x: float, y: float) -> float:
        """
        Multiply two numbers.
        
        Args:
            x: First number
            y: Second number
            
        Returns:
            float: Product of x and y
        """
        return x * y
    
    def divide(self, x: float, y: float) -> float:
        """
        Divide x by y.
        
        Args:
            x: Numerator
            y: Denominator
            
        Returns:
            float: Quotient of x divided by y
            
        Raises:
            ZeroDivisionError: If y is zero
        """
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return x / y