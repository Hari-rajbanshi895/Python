# Map, Filter and Reduce in python
# map
def cube(x):
    return x * x * x

print(cube(3))

l = [1,2,5,4,5]
newl = []
for item in l:
    newl.append(cube(item))
newl = list(map(cube,l))
print(newl)

# Filter

# l = [1,2,4,6,7,4]

# def filter_function(a):
#     return a > 2

# newl = list(filter(filter_function,l))
# print(newl)

# name = ["himal","hari","raju","ramesh"]

# Reduce

# from functools import reduce

# l = [1,2,3,4,5,5]
# sum = reduce(lambda x,y:(x+y)/2,l)
# print(sum)




