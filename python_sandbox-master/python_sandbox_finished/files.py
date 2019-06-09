# Python has functions for creating, reading, updating, and deleting files.

# Open a file/create
myFile = open('myFile.txt', 'w')

# Get some info
print('name: ', myFile.name)
print('is Closed; ', myFile.closed)
print('opening Mode: ', myFile.mode)

# Wright to file 
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Get some info
print('name: ', myFile.name)
print('is Closed; ', myFile.closed)
print('opening Mode: ', myFile.mode)

# Append to file 
myFile = open('myFile.txt', 'a')
myFile.write('I also like PHP')
myFile.close()

# Read from file
myFile = open('myFile.txt', 'r')
text = myFile.read(100)
print(text)
myFile.close()
