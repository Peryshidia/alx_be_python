class BankAccount:
    """
    A class representing a bank account with basic banking operations.
    """
    
    def __init__(self, initial_balance: float = 0.0):
        """
        Initialize a new bank account with an optional initial balance.
        
        Args:
            initial_balance (float): The initial balance of the account. Defaults to 0.0.
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit.
            
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.account_balance += amount
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account if sufficient funds are available.
        
        Args:
            amount (float): The amount to withdraw.
            
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds.
            
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
            
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self) -> None:
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")