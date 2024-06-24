# CREATE TWO TYPES OF BANK ACCOUNT
# FIRST BANK ACCOUNT: IT'S A NORMAL BANK ACCOUNT, WITH DEPOSIT , WITHDRAWAL AND BALANCE DISPLAY FUNCTIONS
# SECOND BANK ACCOUNT: A BANK ACCONT WITH THE CALCULATE OF INTEREST FUNCTION
# WRITE A DOC STRING FOR EACH FUNCTION AND CLASS



class BankAccount():
    """
    A class used to represent a Bank Account.

    Attributes:
    number_bank_account (str): The bank account number.
    balance (float): The balance of the bank account.

    Metods:
    deposit(): Deposits money into the bank account.
               Returns:
               str: A string showing the bank account number and the updated balance.

    withdrawl(): Withdraws money from the bank account. 
                 Returns:
                 str: A string showing the bank account number and the updated balance.
    
    display_balance(): Displays the current balance of the bank account.
                       Returns:
                       str: A string showing the bank account number and the current balance.
    """
    
    def __init__(self, number_bank_account, balance = 0):
        self.number_bank_account = number_bank_account
        self.balance = balance
    
    # Function to calculate the balance + money to deposit entered by the user
    def deposit(self): 
        try:
            money_to_deposit = float(input("How much do you want to deposit?\n€"))
            if money_to_deposit < 0:
                raise ValueError("The deposit amount cannot be negative.")
            self.balance += money_to_deposit
            print("Deposit confirmed.")
            print(f"You deposited: €{money_to_deposit:.2f}")
            return self.display_balance()
            
        except ValueError as error:
            return f"Error {error}"
    
    # Function to calculate the balance - money to withdraw entered by the user
    def withdrawal(self): 
        try:
            money_to_withdraw = float(input("How much do you want to withdraw?\n€"))
            if money_to_withdraw < 0:
                raise ValueError("The deposit amount cannot be negative.")
            if money_to_withdraw > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= money_to_withdraw
            print("Withdraw confirmed.")
            print(f"You withdrew: €{money_to_withdraw:.2f}")
            return self.display_balance()
        except ValueError as error:
            return f"Error: {error}"
    
    # Function to display the balance
    def display_balance(self): 
        return f"Number bank account: {self.number_bank_account}\t\tBalance: €{self.balance:.2f}"


class BankAccountWithInterest(BankAccount):
    """
    A class used to represent a Bank Account with interest, inheriting from BanckAccount.

    Attributes:
    number_bank_account (str): The bank account number.
    balance (float): The balance of the bank account.
    interest (float): The interest rate applied to the bank account.
    
    Metods:
    calculation_interes(): alculates the new balance with interest applied.
                           Returns:
                           str: A string showing the bank account number and the new balance with interest applied.
    """
    def __init__(self, number_bank_account, balance = 0, interest_rate = 0.05):
        super().__init__(number_bank_account, balance)
        self.interest_rate = interest_rate

    # Function that calculate the new balance with interest
    def calculation_interest(self): 
        try:
            if self.interest_rate < 0:
                raise ValueError("Interest rate cannot be negative.")
            self.balance = float(input("What is your balance?\n€"))
            interest = self.balance * self.interest_rate # Calculation of interest
            print(f"Interest earned: €{interest:.2f}")
            self.balance += interest # Deposit interest in to the balance
            return self.display_balance()
        except ValueError as error:
            return f"Error: {error}"
        
#account1 = BanckAccount(1, 5000)
#print(account1.deposit())
#print(account1.withdrawl())
#account1 = BankAccountWithInterest(1, 3500, 0.1)
#print(account1.calculation_interest())

def main():
    """
    Simulates a bank account management system where the user can perform operations
    such as deposit, withdrawal, display balance, and optionally calculate interest earned.

    Initializes the BankAccount and BankAccountWithInterest objects and interacts with the user through a menu:
    - 'Deposit': Allows the user to deposit money into the account.
    - 'Withdrawal': Allows the user to withdraw money from the account.
    - 'Display balance': Shows the current balance of the account.
    - 'Exit': Terminates the program.

    After handling user operations, prompts the user to calculate interest earned on the
    bank account if desired.

    Note:
    - Assumes BankAccount and BankAccountWithInterest classes are defined and accessible.
    - Handles user inputs case insensitively by capitalizing user input for operations.
    - Displays appropriate messages for invalid choices.
    """


    account1 = BankAccount(1)
    account1 = BankAccountWithInterest(1, 0, 0.1)
    choice = ""

    while choice != "Exit":
        choice = input("What do you want to do:\n").capitalize()
        
        if choice == "Deposit":
            print(account1.deposit())
        elif choice == "Withdrawal":
            print(account1.withdrawal())
        elif choice == "Display balance":
            print(account1.display_balance())
        elif choice == "Exit":
            print("Exit from bank account...")
        else:
            print("Invalid choice. Please choose a valid option.")
    
    #CHECKING IF USER WANT TO CALCULATE THE INTEREST EARNED ON BANK ACCOUNT
    answare = ""
    while True:
        answare = input("Do you want to calculate your interest earned on your bank account?\n").capitalize()
        
        if answare == "Yes":
            print(account1.calculation_interest())
        elif answare == "No":
            print("Exit from bank account...")
        else:
            print("Invalid choice. Please choose a valid option.")
        break

         
main()



