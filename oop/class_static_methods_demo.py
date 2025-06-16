class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Static method to add two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of the two numbers
        """
        return a + b
    
    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        Class method to multiply two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of the two numbers
        """
        print(f"Performing {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Using static method
    result1 = Calculator.add(5, 3)
    print(f"Addition result: {result1}")  # Output: Addition result: 8
    
    # Using class method
    result2 = Calculator.multiply(4, 6)
    print(f"Multiplication result: {result2}")  # Output: Performing Arithmetic Operations
                                                      # Multiplication result: 24
    
    # Demonstrating that static method can't access class attributes
    try:
        Calculator.add(2, 3, calculation_type="Custom")  # This will raise an error
    except TypeError as e:
        print(f"Error: {e}")
    
    # Demonstrating that class method can access class attributes
    Calculator.calculation_type = "Custom Operations"
    result3 = Calculator.multiply(2, 3)
    print(f"New multiplication result: {result3}")  # Output: Performing Custom Operations
                                                         # New multiplication result: 6