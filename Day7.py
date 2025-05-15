""" FUNCTIONS IN PYTHON ""
"" BUILT_IN FUNCTION """
""" USER_DEFINED FUNCTION"""

# a = 20
# b = 10
# gmean = (a+b)/(a-b)
# print(gmean)


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# def calculatemean(a,b): # USER_DEFINED FUNCTION
#     mean = (a*b)/(a-b)  
#     print("The mean is:",mean)
#     if(a>b):
#         print("a is grater than b")
#     else:
#         print("b is greater and equal")    

# calculatemean(a,b)

""" WAP TO SHOW MULTIPLICATION TABLE USING FUNCTION"""

# value = int(input("Enter the number: "))

# def mul(value):
#     for i in range(1,11):
#         mul1 = value*(i)
#         print(value,"X",i,"=",mul1)

# mul(value)

""" WAP  to check whether the number is positive or negative """

# num = int(input("Enter the number: "))

# def check(num):
#     if num>0:
#         print('The number is positive')
#     else:
#         print('The number is negative')

# check(num)

"""Arguments in Function"""
# It is necessary to pass the argument in correct positional order
# and the number of argument passwd should match with actual function def.

# def average(a,b):
#     print("The average is",(a+b)/2)

# average(4,8)

# def name(fname,mname="chandra singh",lname="Rajbanshi"):
#     print("My name is",fname,mname,lname)

# name(fname= 'hari',mname="law")


# def average(*num): #Tuple
#     print(type(num))
#     sum = 0
#     for i in num:
#         sum = sum + i
#         print('The average is', sum / len(num))

# average(1,3,4)

# def name(**name):# Dictionary
#     print(type(name))
#     print("My name is", name["fname"],name["mname"],name["lname"])

# name(mname = "Chandra Singh",fname = "Hari",lname="Rajbanshi")

'''Recursion in python'''
    # => The ability of function to call itself within function is called recursion

# Example
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(4))
# 4 * 3 * 2 * 1 (factorial(4))
# 3 * 2 * 1 (factorial(3))

'''WAP to print * '''
# In this order
# *
# * *
# * * *
# def pattern(n):
#     if(n==0):
#         return
#     print('*' * n)
#     pattern(n-1)

# pattern(5)
    
