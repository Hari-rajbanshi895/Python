# string formatting in python
# Fstring

# name ="Himal"
# country = "Nepal"

# txt  = "my name is {} and i am from {}"

# print(txt.format(name,country))

# txt =  f"my name is {{name}} and i am from {{country}}"
# print(txt)

# txt =  f"my name is {name} and i am from {country}"
# print(txt)

# price = 49.59785438
# print(f"for only {price:.2f}$")

# Docstring in python
'''Docstrings are also used for documentation in program'''

def factorial(a,b):
    ''' calcute two numbers'''
    add = a + b
    print(add)

factorial(5,4)
print(factorial.__doc__)

def square(n):
    ''' takes in a number and return the squre of n'''
    print(n**2)

print(square.__doc__)