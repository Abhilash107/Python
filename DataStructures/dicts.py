student = {
    "name": "Abhilash",
    "age": 22,
    "cgpa": 8.88
}

print(student)
print(student["name"])

# get() ⭐⭐⭐
#& Safer when the key might not exist.
print(student.get("name"))
# If the key doesn't exist: then returns None
print(student.get("name", "Not available"))
print(student.get("address", "Not available"))


# for i in student:
#     print(i," :  ", student[i])


# Keys must be unique
# The second value replaces the first.

data = {
    "hello": [1, 2]
}

# print(data)

student["city"] = 'Bhubhaneswar'
student['age'] = 26

print(student.keys())#returns a set-liked object
print(student.values())#returns a object
print(student.items())#returns a set-like object providing a view on the dict's items.


age = student.pop('age')

student.update({
    "age": 23,
    "city" : "delhi"
})

student.clear()



