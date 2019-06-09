# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# Sample Json
userJson = '{"first_name": "Jhon", "last_name": "Doe", "age": 30}'

# Parse to Dict
user = json.loads(userJson)

print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJson = json.dumps(car)
print(carJson)