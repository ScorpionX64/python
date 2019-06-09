# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class
class user:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1

# exstend class
class customer(user):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance
    
    # overide base clase greeting method
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# init user object
brad = user('brad', 'brad@gmail.com', 37)

# init customer 
janet = customer('Janet Johnson', 'Janet@yahoo.com', 25)

janet.set_balance(500)

print(janet.greeting())

print(type(brad))
print(brad.name)
brad.has_birthday()
print(brad.greeting())

