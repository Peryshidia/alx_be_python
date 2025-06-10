import sys
from robust_division_calculator import safe_divide

def print_usage():
    """Display usage instructions."""
    print("Usage: python main.py <numerator> <denominator>")
    print("\nExample: python main.py 10 2")
    print("This will calculate 10 divided by 2")

def main():
    """Main function to handle command-line division operations."""
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)
    
    # Get numerator and denominator from command line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    
    # Perform division
    success, result = safe_divide(numerator, denominator)
    
    if success:
        print(f"\n{numerator} ÷ {denominator} = {result:.2f}")
    else:
        print(f"\n{result}")
        sys.exit(1)

if __name__ == "__main__":
    main()