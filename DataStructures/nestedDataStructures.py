# Matrix

mat = [
    [1, 2],
    [3, 4]
]

print(mat)
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j], end=" ")
    print()


#Dict inside list

students = [
    {"name": 'A', "age": 23},
    {"name": 'B', "age": 22}
]

print(students[0]["name"])



# List inside dictionary
student = {
    "name": "Abhilash",
    "skills": ["Java", "Python", "Node.js"]
}
print(student["skills"][0])


# Dictionary inside dictionary
users = {
    "user1": {
        "name": "A",
        "age": 22
    }
}

print(users["user1"]["name"])