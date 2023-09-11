class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        elif amount > self.__account_balance:
            return "Insufficient funds. Withdrawal not allowed."
        else:
            return "Invalid withdrawal amount. Please enter a positive value."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ${self.__account_balance}"


my_account = BankAccount("35698","Nivetha",1000)
print(my_account.display_balance())  
print(my_account.deposit(500))       
print(my_account.withdraw(200))    
print(my_account.withdraw(1500))     
print(my_account.display_balance())  
