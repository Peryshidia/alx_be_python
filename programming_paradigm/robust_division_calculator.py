def safe_divide(numerator: str | float, denominator: str | float) -> tuple[bool, float | str]:
    """
    Safely perform division with comprehensive error handling.
    
    Args:
        numerator: The number to be divided (can be string or float)
        denominator: The number to divide by (can be string or float)
        
    Returns:
        tuple[bool, float | str]: A tuple containing:
            - bool: True if division was successful, False if there was an error
            - float | str: The division result if successful, error message if not
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Check for division by zero
        if den == 0:
            return False, "Error: Division by zero is not allowed"
            
        # Perform division
        result = num / den
        return True, result
        
    except ValueError:
        return False, "Error: Both inputs must be valid numbers"
    except Exception as e:
        return False, f"Error: An unexpected error occurred - {str(e)}"