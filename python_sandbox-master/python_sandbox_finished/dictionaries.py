# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create 
person = {
    'first_name' : 'Jhon',
    'last_name' : 'Doe',
    'age' : 30
}

print(person)

# Use constructor
person1 = dict(first_name='Sara', last_name='Williams', age=28)

print(person1)

# Get value
print(person['first_name'])

print(person.get('last_name'))

# Add key value
person['phone'] = '123-123-123'
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items)

# Copy dict
person2 = person.copy()
person2['city'] = 'boston'
print(person2)

# Remove item
del(person['age'])

person.pop('phone')

print(person)

# Clear
person.clear()

print(person)

# Get length
print(len(person1))

# list of dict

people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevan', 'age': 25}
]

print(people)
print(people[1]['name'])

