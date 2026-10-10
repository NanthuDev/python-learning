class BankAccount:
     def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
     def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid deposit amount")