#Example: Simple OOP Project – Bank Account
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


account = BankAccount("Raj", 10000)

account.deposit(2000)
account.withdraw(3000)
account.show_balance()