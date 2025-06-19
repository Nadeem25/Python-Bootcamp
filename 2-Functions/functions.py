# Positional Arguments
def positional_arguments(*pargs) :
    for arg in pargs:
     print(f"Positional Arguments Value: {arg}")

positional_arguments(1,4,5,7, 'Nadeem', 'Krish')

# Keyword Arguments
def keyword_argument(**kwargs):
   for key, value in kwargs.items():
      print(f"Keyword Argument key : {key} value : {value}")
keyword_argument(name="Jack", age=34)


# Positional and Keyword Arguments
def pos_key_argument(*pargs, **kwargs):
   
    for arg in pargs:
     print(f"Positional Arguments Value: {arg}")
    
    for key, value in kwargs.items():
      print(f"Keyword Argument key : {key} value : {value}")

pos_key_argument(1,2,39,0, student_id=12345, student_name="Jack")


# =========== Lambda Function =============
# It is anonymous function (function without name) and define using lambda keyword.
# They can have many number of arguments but only one expression. It is use for short operations or as arguments to higher order function.

# Syntax
#lambda arguments(multiple): expression(simple)
addition = lambda a,b: a+b
print(f"Lambda functin sum value: {addition(6, 8)}")

# ============ Map ==================
def sequares(number):
   return number * number
      
print(f"Using map function: {list(map(sequares, [1,4,6,7,8]))}")
print(f"Map function with lambda: {list(map(lambda x:x*x, [2, 4, 6, 7]))}")

# Map with multiples input arguments
numbers1 = [2, 4, 6]
numbers2 = [3,5]
multiplication = list(map(lambda x,y, z: x*y*z, numbers1, numbers2, numbers1))
print(f"Map with multiple arguments output: {multiplication}")


# Map with inbuilt function
words = ['Bananen', 'Apfel', 'Zitrone']
print(f"Map with inbuild functin: {list(map(str.upper, words))}")

# =================== filter ==========================
num = [1,2,3,4,5,6,7,8,9]
even_and_greater_than_five = list(filter(lambda x: x>5 and x%2==0, num))
print(f"Filter function: {even_and_greater_than_five}")