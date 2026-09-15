import json

# JSON → Python
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)
print(data['name'])


# python -> json

student = {
    'Name': 'Tony',
    'Age' : 23
}

with open('data.json', 'w') as file:
    json.dump(student, file)

#& loads()

# JSON string → Python object
# json.loads('{"name": "Abhilash"}')

#& dumps()

# Python object → JSON string
# json.dumps({"name": "Abhilash"})