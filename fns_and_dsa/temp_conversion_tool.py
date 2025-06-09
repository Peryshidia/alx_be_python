# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
        
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def get_temperature_input() -> tuple[float, str]:
    """
    Get temperature and unit from user input with validation.
    
    Returns:
        tuple[float, str]: Temperature value and unit ('C' or 'F')
        
    Raises:
        ValueError: If temperature is not a valid number
    """
    try:
        temp = float(input("Enter the temperature: "))
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()
        
        if unit not in ['C', 'F']:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
        return temp, unit
    except ValueError as e:
        if "could not convert string to float" in str(e):
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        raise

def main():
    """
    Main function to run the temperature conversion program.
    """
    print("=== Temperature Conversion Tool ===")
    
    try:
        temperature, unit = get_temperature_input()
        
        if unit == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"\n{temperature}°F = {celsius:.2f}°C")
        else:  # unit == 'C'
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"\n{temperature}°C = {fahrenheit:.2f}°F")
            
    except ValueError as e:
        print(f"\nError: {str(e)}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()