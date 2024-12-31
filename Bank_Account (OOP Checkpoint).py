""""Create a class called "Account" that has the following attributes:
account_number (string), account_balance (float), and account_holder (string)
The class should have the following methods:
deposit(amount: float) - This method should add the amount passed as an argument to the account balance.
withdraw(amount: float) - This method should subtract the amount passed as an argument from the account balance, but only if the account balance is greater than the amount being withdrawn.
check_balance() - This method should return the current account balance."""

# Define the Account class and its attributes as specified above.
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

# Define the deposit() method. It should take in one argument, the amount to be deposited, and add it to the account balance.
    def deposit(self, amount):
        self.balance += amount
        return(f"Deposited ${amount}. New balance: ${self.balance}")

# Define the withdraw() method. It should take in one argument, the amount to be withdrawn, and subtract it from the account balance. The method should only execute the withdrawal if the account balance is greater than or equal to the amount to be withdrawn.
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

# Define the check_balance() method. It should return the current account balance.
    def check_balance(self):
        return self.balance

# Create an instance of the Account class, and assign it to a variable called "my_account".
my_account = Account("100567189", "Eno Peters", 1000)

# Use the methods of the class to deposit and withdraw money from the account, and check the account balance.
my_account.deposit(500)
my_account.withdraw(200)
print("Current balance:", my_account.check_balance())

# More operations 
my_account.deposit(200)
my_account.withdraw(800)
print("Current balance:", my_account.check_balance())

my_account.deposit(0)
my_account.withdraw(1000)
print("Current balance:", my_account.check_balance())


