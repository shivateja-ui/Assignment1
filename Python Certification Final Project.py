from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
        else:
            print("Insufficient funds!")
class SavingsAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds!")
class BusinessAccount(Account):
    def __init__(self, account_number, balance=0, credit_limit=5000):
        super().__init__(account_number, balance)
        self.credit_limit = credit_limit
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance + self.credit_limit - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds!")
account_type = input("Enter the account type (1 = Checking, 2 = Savings, 3 = Business): ")
account_number = input("Enter the account number: ")
if account_type == "1":
    account = CheckingAccount(account_number)
elif account_type == "2":
    account = SavingsAccount(account_number)
elif account_type == "3":
    account = BusinessAccount(account_number)
else:
    print("Invalid account type!")
    exit()
while True:
    print("\nSelect an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    option = input("Enter option number: ")
    if option == "1":
        amount = float(input("Enter the deposit amount: "))
        account.deposit(amount)
        print("Deposit successful!")
    elif option == "2":
        amount = float(input("Enter the withdrawal amount: "))
        account.withdraw(amount)
    elif option == "3":
        account.display_balance()
    elif option == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")