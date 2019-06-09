# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create a Tuple
fruits = ('Apples', 'Oranges', 'Grapes')
print(fruits)

fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
print(fruits2)

fruits3 = ('Apples')
print(type(fruits3))

fruits4 = ('Apples',) # single value needs trailing ,
print(type(fruits4))

# Get value
print(fruits[1])

# can't change value
# fruits[1] = 'Pear' # gives error as tuple is unchangeable

# Delete tuple

del fruits

# print(fruits)

# get length 
print(len(fruits2))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# create set 
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set 
print('Apples' in fruits_set)

# add to set
fruits_set.add('Grape')
print(fruits_set)

# renove from set
fruits_set.remove('Grape')
print(fruits_set)

# add duplicat
fruits_set.add('Apples')
print(fruits_set)

# clear set
fruits_set.clear()
print(fruits_set)

# delete set
del fruits_set



