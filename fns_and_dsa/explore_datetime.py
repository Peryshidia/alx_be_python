from datetime import datetime, timedelta

def display_current_datetime() -> None:
    """
    Display the current date and time in a formatted string.
    """
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_datetime}")

def calculate_future_date() -> None:
    """
    Calculate and display a future date based on user input.
    """
    try:
        days = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Date after {days} days: {formatted_future_date}")
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")

def main():
    """
    Main function to run the datetime exploration program.
    """
    print("=== Date and Time Exploration ===")
    
    # Part 1: Display current date and time
    print("\nPart 1: Current Date and Time")
    display_current_datetime()
    
    # Part 2: Calculate future date
    print("\nPart 2: Future Date Calculation")
    calculate_future_date()

if __name__ == "__main__":
    main()