# Encapsulation: It is the concept of wrapping the data (variable) and methods (function) together as single unit.

class Person:
    def __init__(self, name, salary, age):
        self.name = name # Public Variable
        self._age = age # protected Variable
        self.__salary = salary # Privable Variable


# ======== Access Modifier ==================
# 1. Private: Private variable cannot be access outside the class

person = Person("Jack", 345556, 56)
#print(person.__salary)
#print(person.__age) # Error: 'Person' object has no attribute '__age'


# 2. Protected : 
# --> Access within class
# --> Access Within sub-class
# --> Access outside the class but prohibited
class Employee(Person):
     def __init__(self, name, salary, age, emp_id):
          self._emp_id = emp_id
          super().__init__(name, salary, age)
          #self._age = 90

employee = Employee('Krish', 4556, 40, "D1234")
print(f"Accessing Protected element in child class : {employee._age}")
print(f"Accessing protected variable outside the class: {employee._emp_id}")


# Encapsulation with setter and getter
class BankAccount:
     def __init__(self, account_no, account_type):
          self.__account_no = account_no
          self.account_type = account_type

     def get_account_no(self):
          return self.__account_no
     
     def set_account_no(self, account_no):
          self.__account_no = account_no

bank_account = BankAccount(12345, "Saving")
bank_account.get_account_no()
bank_account.set_account_no(5678)