
# Iterating through Dictionaries
# Iterate through the dictionary student and print all keys.
# Iterate through the dictionary student and print all values.
# Iterate through the dictionary student and print all key-value pairs in the format key: value.
# Check if the key grade exists in the student dictionary and print True or False.
# Count the total number of keys in the student dictionary.


student = {
    "name":"M.Adell",
    "age": 20 ,
    "class":"BSSE",
    "UNiversity":"NUMl",
    "Grade":"A+"
}
count=0
for   key ,value in  student.items():
    
    print (key ,":" , value )
    count+=1
print ("total number of keys",count)

var = len(student)
print ("lent of student ",var)

for kye in student:
    if key == "Grade":
        print(True)
    else:
        print(False)