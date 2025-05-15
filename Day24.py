# Difference between "==" and "is"
a = 2
b = 2
print(a is b) # exact memory location (immutable)
print(a==b) # values

a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a == b) 

a = (1,2,3)
b = (1,2,3)
print(a is b)
print(a == b) 

name = "himal"
fname = "himal"
print(f" The value is: ", {name} is {fname})
print(f" The value is: ", name == fname)