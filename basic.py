## 1. Python uses indentation to define blocks of code.
age = 23
if age > 40:
    print('I am rich')

# Multiple statements on a single lines
x = 5; y = 10; z = x+y
print(z)

## Type inference
variable = 10
print(type(variable)) ## <class 'int'>
variable = "Krish"
print(type(variable)) ## <class 'int'>

## The input is in str data type bydefault
age = int(input("Enter the age"))