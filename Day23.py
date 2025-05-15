# lambda dunction in python

# def cube(x):
#     return x*x*x
# print(cube(2))

# a = lambda x:x*2
# print(a(2))

# x = lambda a,b : a+b
# print(x(2,4))

def average(a,b):
    return lambda  a,b:(a+b)/2
print(average(3,4))
