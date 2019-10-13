import json

with open('data.json', 'r') as obj:
    data = json.load(obj)
    for p in data:
        print(p['email']) 