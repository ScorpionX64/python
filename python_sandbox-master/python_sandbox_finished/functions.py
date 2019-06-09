# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
    print(f'Hello {name}')

sayHello('Jhon Doe')

# Create function with default value for input param
def sayHello1(name='Sam'):
    print(f'Hello {name}')

sayHello1()

# Return function
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(6, 4)
print(num)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum1 = lambda num1, num2 : num1 + num2

print(getSum1(10, 3))