# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]

numbers2 = list((1, 2, 3, 4, 5))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

print(numbers, numbers2)

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

print(fruits)

# Remove from list
fruits.remove('Grapes')

print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')

print(fruits)

# Remove with pop
fruits.pop(2)

print(fruits)

# Revers list
fruits.reverse()

print(fruits)

# Sort list
fruits.sort()

print(fruits)

# Revers sort
fruits.sort(reverse = True)

print(fruits)

# Change value
fruits[0] = 'blueberries'

print(fruits)