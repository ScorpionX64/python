# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core modules
import datetime
from datetime import date
import time
from time import time

# Pip modules
#import camelcase
from camelcase import CamelCase

# import custom module
import validator
from validator import validate_email

today = datetime.date.today()

print(today)

# Import derived libary
#import datetime
#from datetime import date

now = date.today()
print(now)

#timestamp = time.time()
#print(timestamp)

# import method from module
#from time import time
timestamp1 = time()
print(timestamp1)

# install module usint pip3 in termenal
#pip3 install camelcase

# to see all installed modules
#pip3 freeze

c = CamelCase()
print(c.hump('hello there world'))

email = 'test@test.com'
email1 = 'test#test.com'
if validate_email(email1):
    print('email is valid')
else:
    print('email is bad')