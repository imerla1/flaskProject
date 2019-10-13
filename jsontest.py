import json

with open('data.json', 'r') as obj:
    data = json.load(obj)
    email = data[0]['email']
    password = data[0]['password']
    print(email)
    print(password)
