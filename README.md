# Object-oriented-programming-OOP-for-Bank-Account
This project demonstrates Object-Oriented Programming (OOP) principles by creating an `Account` class to simulate a basic bank account system. 

## Features
The `Account` class includes the following attributes and methods:

### Attributes
1. **`account_number` (string)**: Unique identifier for the account.
2. **`account_holder` (string)**: Name of the account holder.
3. **`balance` (float)**: The current balance of the account (default is 0).

### Methods
1. **`deposit(amount: float)`**:
   - Adds the specified amount to the account balance.
   - Returns a confirmation message with the updated balance.

2. **`withdraw(amount: float)`**:
   - Deducts the specified amount from the account balance.
   - Ensures the withdrawal does not exceed the current balance.
   - Prints an error message if funds are insufficient.

3. **`check_balance()`**:
   - Returns the current account balance.

## How It Works
### Creating an Account
An instance of the `Account` class is initialized with:
- `account_number` (string)
- `account_holder` (string)
- Optional `balance` (float, default is 0)

Example:
```python
my_account = Account("100567189", "Eno Peters", 1000)
```

### Using Account Methods
- **Deposit Money**:
  ```python
  my_account.deposit(500)
  # Deposited $500. New balance: $1500
  ```
- **Withdraw Money**:
  ```python
  my_account.withdraw(200)
  # Withdrew $200. New balance: $1300
  ```
- **Check Balance**:
  ```python
  print("Current balance:", my_account.check_balance())
  # Current balance: $1300
  ```

## Sample Usage
```python
# Create an account
my_account = Account("100567189", "Eno Peters", 1000)

# Perform transactions
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
```

### Output:
```plaintext
Deposited $500. New balance: $1500
Withdrew $200. New balance: $1300
Current balance: 1300
Deposited $200. New balance: $1500
Withdrew $800. New balance: $700
Current balance: 700
Deposited $0. New balance: $700
Withdrew $1000. Insufficient funds.
Current balance: 700
```

## Learning Objectives
- Understand OOP concepts such as attributes and methods.
- Implement encapsulation and data validation in Python classes.
- Practice writing reusable and modular code.

## How to Run
1. Copy the code into a Python file (e.g., `account.py`).
2. Run the script using Python:
   ```bash Bank_Account (OOP Checkpoint).py ```


## Contributions
Feel free to contribute by:
- Adding more features (e.g., account type, transaction history).
- Enhancing error handling or validations.
- Writing unit tests for the `Account` class.

---

Happy coding! 🎉
```
