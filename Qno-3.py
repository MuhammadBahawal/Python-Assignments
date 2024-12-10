# Advanced Dictionary Usage
# Merge the following two dictionaries and print the result:
# dict1 = {'a': 1, 'b': 2}  
# dict2 = {'c': 3, 'd': 4}  
# Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
# Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.
# Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.
# Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).

dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4}  

dict = dict1 | dict2
print (dict)

dict1.update(dict2)
dict3 = dict1
print(dict3)


dict4 = {
   tuples :  [('name', 'Alice'), ('age', 25), ('city', 'Paris')]
}
print(dict4)



