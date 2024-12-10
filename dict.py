# Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.

# Access the value of the key grade in the student dictionary.

# Add a new key city to the student dictionary and set its value to "New York".

# Update the value of the age key in the student dictionary to 20.

# Remove the key city from the student dictionary.


# students = {
#     "name": "bahawal",
#     "age": 20 ,
#     "grade": "A+",
# }
# students["city"] = "New York"
# students["age"] = 29
# del students["city"]
# print(students)




# Iterating through Dictionaries

# Iterate through the dictionary student and print all keys.

# Iterate through the dictionary student and print all values.

# Iterate through the dictionary student and print all key-value pairs in the format key: value.

# Check if the key grade exists in the student dictionary and print True or False.

# Count the total number of keys in the student dictionary.


# students = {
#     "name": "bahawal",
#     "age": 20 ,
#     "grade": "A+",
# }

# for value  in students.values():
#     print(value)

# for key , value in students.items():
#     print(key , " : ",  value)

# if "grade" in students:
#     print(True)
# else:
#     (False)

# print(students.__len__())

# Advanced Dictionary Usage
# Merge the following two dictionaries and print the result:

# dict1 = {'a': 1, 'b': 2}  
# dict2 = {'c': 3, 'd': 4}  


# dict1 = {'a': 1, 'b': 2}  
# dict2 = {'c': 3, 'd': 4}
# dict1.update(dict2)
# print(dict1)
# another method to add two dictionaries is with unpacking operator that is ** (double star or double multiple sign)

# total = {**dict1, **dict2}
# print(total)

# Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
# dict = {"name": "Alice",
#         "age": 25,
#         "city": "Paris",
#         }

# dict = {'z': 1, 'a': 2, 'c': 3}

# sorted_dictionary = sorted(dict.keys())
# print(sorted_dictionary)

# Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.

# dict = {'z': 1, 'a': 2, 'c': 3}
# reversed_dictionary = {value: key for key, value in dict.items()}
# print(reversed_dictionary)

# Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.

# dict = {'z': 1, 'a': 2, 'c': 3}
# ass_dict = sorted(dict.keys())
# print(ass_dict)

# Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).

# dict1 = {'a': 1, 'b': 2}  
# dict2 = {'c': 3, 'd': 4}  

# def check_identical(dict1, dict2):
#     return dict1 == dict2
# print(check_identical(dict1, dict2))


# Nested Dictionaries

# Create a nested dictionary to represent the following data:
# Person:  
#   Name: John  
#   Age: 30  
#   Address:  
#     Street: 123 Elm St  
#     City: Boston  
   
# person = {
#     "Name": "John",
#     "Age": 30,
#     "Address": {
#         "Street": "123 Elm St",
#         "City": "Boston",
#     },
# }
# Access the value of the City key in the nested dictionary from the previous question.

# print(access_value)
# access_value = person["Address"]["City"]

# Add a new key Phone to the nested dictionary with the value "123-456-7890".
# person["Address"]["Phone"] = "123-456-7890"

# Delete the Address key from the nested dictionary.

# del person["Address"]

# Iterate through all the keys in the outermost level of the nested dictionary and print them.

# for key in person.keys():
#     print(key)
    


# Applications of Dictionaries
# Use a dictionary to count the occurrences of each word in the string "hello world hello python world".


# text = "hello world hello python world"
# words = text.split()

# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print(word_count)




# Write a Python program to find the key with the maximum value in the dictionary {'a': 10, 'b': 15, 'c': 7}.

# data = {'a': 10, 'b': 15, 'c': 7}

# max_key = max(data, key=data.get)

# print(f"The key with the maximum value is: {max_key}")

# Using dictionary comprehension



# Create a dictionary to map numbers 1 to 5 to their squares (e.g., {1: 1, 2: 4, 3: 9, ...}).

# squares = {x: x**2 for x in range(1, 6)}

# print(squares)


# Write a Python program to remove duplicate values from the dictionary {'a': 10, 'b': 15, 'c': 10, 'd': 15}.


# data = {'a': 10, 'b': 15, 'c': 10, 'd': 15}

# unique_dict = {}
# seen_values = set()  

# for key, value in data.items():
#     if value not in seen_values:
#         unique_dict[key] = value
#         seen_values.add(value)

# print(unique_dict)

# Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return "Key not found".

# def get_value(dictionary, key):
#     return dictionary.get(key, "Key not found")

# data = {'a': 10, 'b': 15, 'c': 7}
# key_to_find = 'b'
# print(get_value(data, key_to_find)) 
# key_to_find = 'z'
# print(get_value(data, key_to_find))  

# Challenging Problems
# Given two dictionaries dict1 = {'a': 5, 'b': 10} and dict2 = {'a': 3, 'b': 7}, write a Python program to add the values of matching keys and print the result.

# dict1 = {'a': 5, 'b': 10}
# dict2 = {'a': 3, 'b': 7}

# # Use dictionary comprehension to add values of matching keys
# result = {key: dict1[key] + dict2.get(key, 0) for key in dict1}

# print(result)

# Write a Python program to create a dictionary where the keys are the first n positive integers, and the values are their cubes. Take n as user input.

# n = int(input("Enter the value of n: "))

# cubes = {x: x**3 for x in range(1, n + 1)}

# print(cubes)

# Flatten the following nested dictionary into a single-level dictionary:
# {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}  

# nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}

# def flatten_dict(d, parent_key='', sep='.'):
#     flat_dict = {}
#     for key, value in d.items():
#         new_key = f"{parent_key}{sep}{key}" if parent_key else key
#         if isinstance(value, dict):
#             flat_dict.update(flatten_dict(value, new_key, sep))
#         else:
#             flat_dict[new_key] = value
#     return flat_dict

# flattened = flatten_dict(nested_dict)
# print(flattened)

# Write a Python program to split a dictionary into two based on whether the values are odd or even.

# Input dictionary
# data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# odd_dict = {}
# even_dict = {}

# for key, value in data.items():
#     if value % 2 == 0:
#         even_dict[key] = value
#     else:
#         odd_dict[key] = value

# print("Odd values dictionary:", odd_dict)
# print("Even values dictionary:", even_dict)

# Create a dictionary comprehension to filter out all keys in {'a': 1, 'b': 2, 'c': 3, 'd': 4} where the value is less than 3.

# data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# filtered_dict = {key: value for key, value in data.items() if value >= 3}

# print(filtered_dict)

