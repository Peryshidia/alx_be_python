import sys
from bank_account import BankAccount

def print_usage():
    """Display usage instructions."""
    print("Usage: python main-0.py <command>:<amount>")
    print("Commands:")
    print("  deposit:<amount>  - Deposit money into the account")
    print("  withdraw:<amount> - Withdraw money from the account")
    print("  display          - Show current balance")
    print("\nExample: python main-0.py deposit:100")

def main():
    """Main function to handle command-line banking operations."""
    # Initialize account with $100 starting balance
    account = BankAccount(100)
    
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    try:
        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None

        match command.lower():
            case "deposit":
                if amount is None:
                    print("Error: Amount required for deposit")
                    sys.exit(1)
                account.deposit(amount)
                print(f"Deposited: ${amount:.2f}")
                
            case "withdraw":
                if amount is None:
                    print("Error: Amount required for withdrawal")
                    sys.exit(1)
                if account.withdraw(amount):
                    print(f"Withdrew: ${amount:.2f}")
                else:
                    print("Insufficient funds.")
                    
            case "display":
                account.display_balance()
                
            case _:
                print("Error: Invalid command")
                print_usage()
                sys.exit(1)
                
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()