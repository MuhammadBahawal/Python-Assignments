#Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.
# Access the value of the key grade in the student dictionary.
# Add a new key city to the student dictionary and set its value to "New York".
# Update the value of the age key in the student dictionary to 20.
# Remove the key city from the student dictionary.


student = {
    "name": "M.Adeel",
    "age": 25,
    "Grade":"A+"
}

print(student["Grade"])

student["city"]="New York"

student["age"]=20
print(student)

del student["city"]
print(student)