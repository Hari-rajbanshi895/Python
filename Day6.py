"""Tuples in Python"""
"""immutuable"""
"""Allow duplicates"""

# fruits = ('apple','banana','cherry','mango')
# print(type(fruits))
# print(fruits[2])
# print(fruits[-1])

'''To change data of a tuple first you need to convert a tuple
 into list and change data in the list because list us mutable and 
 you need to change the list into tuple 'Notice:- tuples are immutable
 if we do change by converting with list it means it is creating new tuple'
'''

'''
name = ('himal','ayush','radha','damar')
value = list(name) # changed tuple to list
value[1] = 'ram'  # make changes in list
name = tuple(value) # changed back list to tuple
print(name)'''

num = (1,2,3,2,4,3,5,3,5)
print(type(num))
print(num)
change = list(num)
change.sort()
num = tuple(change)
print(num)

num = (1,2,3,2,4,3,5,3,5)
print(type(num))
print(num)
change = list(num)
change.sort(reverse=True)
num = tuple(change)
print(num)