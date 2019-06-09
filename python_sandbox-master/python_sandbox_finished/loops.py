# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Jhon', 'Sara', 'Paul', 'Sussan']

# Simple for loop
for person in people:
    print(person)

print()

# Break
for person in people:
    if person == 'Sara':
        break
    print(person)

print()

# Continue
for person in people:
    if person == 'Sara':
        continue
    print(person)

print()

# Range
for i in range(len(people)):
    print(people[i])

print()

for i in range(0, 10):
    print(f'number {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0

while count <= 10:
    print(count)
    count +=1