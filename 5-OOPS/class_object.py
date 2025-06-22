# Instance variable and Method
class Dog:
    # constructor
    def __init__(self, name, age):
        print(f"Inside constructor")
        self.name = name  # self.name is use to create instance variable
        self.age = age

    def bark(self, sound):
        print(f"{self.name} Sound: {sound}")

dog_obj = Dog('Jack', 30)
dog_obj.bark("Lucy")

# Modelling a Bank Account

# Define a class for Bank Account
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} has deposited. Total Amoutn: {self.balance}")

    def withdraw(self, amount): 
        if(amount > self.balance):
            print(f"Insufficient Fund")
        else:
            self.balance = self.balance - amount
            print(f"{amount} has debited. New balance: {self.balance}")

    def checkBalance(self):
        print(f"Balance Amount is: {self.balance}")
        
bank_account = BankAccount('Nadeem', 2000)
print(f"=========================================")
bank_account.deposit(2000)
bank_account.withdraw(1000)
bank_account.checkBalance()