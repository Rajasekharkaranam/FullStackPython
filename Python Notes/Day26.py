#Example: Encapsulation
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(2000)

print("Balance:", account.get_balance())