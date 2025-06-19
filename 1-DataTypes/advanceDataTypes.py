## 1. List: Lists are ordered collections of items that are mutable. 
# The can contains the item of different data types
colors = ['Weise', 'Gelb', 'Blau', 'Schwarz', 'Rot', 'Grun', 'pink']
vegitables = ['Tomaten', 'Kartoffeln', 'Zwiebeln', 'Zitronen']
print(colors[0])
print(vegitables[-2])
# Modifying list element
colors[2]='Rot'
colors.append('Orange')
colors.insert(1, 'Black')
colors.remove('Black') # Removing 1st occurence of last element
pop_color = colors.pop() # Remove last element

# Iternation
fruits = ['Erdbeeren', 'Bananen']
for fruit in fruits:
    print(f"Fruit:{fruit}")

for index, fruit in enumerate(fruits):
    print(f"Fruit:{fruit} at Index: {index}")

# Slicing list
numbers = [1,2,4,4,5,5,6,7,8,9]
#numbers[startIndex: endIndex]
print(numbers[::]) # Print all the elements
print(numbers[2:5])
print(numbers[2:])
print(numbers[::-1])
print(numbers[::2]) # Print the elements step by 2


#  =========== List Comprehension ==================== 
squarList = []
for x in range(10):
    squarList.append(x**2)
print(f"Original Way:{squarList}")

# Basic Syntax: [expression for item in iterable]
print(f"Comprehension Way: {[x**2 for x in range(10)]}")
print(f"Lenght of words: {[len(word) for word in ["Nadeem", "Jack", "Tom"]]}")

# Conditional Logic: [expression for item in iterable if condition]
even_number = [num for num in range(10) if num%2 == 0]
print(f"Conditional Logic Comprehension: {even_number}")

# Nested Comprehnsion Logic: [expression for item1 in iterable1 for item2 in iternable2]
numbers = [1,2,3,4]
characters = ['a', 'b', 'c', 'd']
paires = [[number, char] for number in numbers for char in characters]
print(f"Nested Comprehension: {paires}")


# ============ 2. Tuples =================================

# It is ordered collection of items that are immutable
empty_tuple = ()

# Accessing Tuple Element
number = (1,2,3,4,5)
print(f"Tuples Element: {number[1]}")

# Tuples are Immutable
# number[1] = "Krish" # Error

# Packing and Unpacking Tuple
pack_tuples = 1, "Hello Everyone", 5.667
print(f"Packed Tuples: {pack_tuples}")

num, word, value = pack_tuples
print(f"Unpacked Tuples: number: {num}, word: {word}, value: {value}")

# Unpacking with *
number_tuple = (1,2,3,4,5)
first, *middle, last = number_tuple
print(first) # 1
print(*middle) # [2,3,4]
print(last) # 5



# ===================== 3. Dictionary ======================
# It is unordered collection of data which is store in key and value pair.
# Key must must be unique and immutable (eg. string, number or tuples) while value can be of any type.
empty_dict = {}
empty_dict = dict()
student = {'name':"Krish", 'age': 32}
print(f"Student AGe: {student['age']}")
print(f"Student Name: {student.get('name')}")

for key, value in student.items():
    print(f"Dictory Key: {key} and Value:{value}")

# 1. Add, Update and Delete Dictioany value
student['address'] = "Mumbai"
student['age'] = 36
del student['address']
student.keys() # all keys
student.values() # all values
student.items() # List of tuples

student.get('location', 'Mumbai') # If location is not in dict then add the location keyword with value

# Nested Dictionay
student_dict = {
    "student1": {'name':"Krish", 'age': 32},
    "student2": {'name':"Krish", 'age': 32}
}
print(f"Student Dictionay: {student_dict['student1']["name"]}")

# Iterating over nested dictory
for student_id, student_info in student_dict.items():
    print(f"Student Id: {student_id} and Student Info: {student_info}")

# Dictionary Comprehension
{num: num**2 for num in range(10) if num%2 == 0}

# Use a dictionay to count the frequency of element in the list
numbers_list = [2, 5, 6,7, 2,3, 4, 8, 9, 1, 2,3]
frequency_dict = {}
for number in numbers_list:
    if number in frequency_dict: 
        frequency_dict[number]+=1
    else :
        frequency_dict[number] = 1

# Merge Dictionary
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}
merged_dict = {**dict1, **dict2}

