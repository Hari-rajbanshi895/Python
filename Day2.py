# name = ("HimalRajbanshi")
# print(name[1:6])

# name = ("HimalRajbanshi")
# print(len(name))
# print(type(name))

num = (1,2,3,4,5,6)
print(num[:3])

# if-else statements
# conditional operators
#  > , < , <= , >= , == , !=

# age = int(input("Enter your age: "))
# print(age)

# if age > 18:
#     print("You can drive")
# else:
#     print("You cannot drive")


# num = [1,2,5,6,78,99,00,4,7]

# user = int(input("Enter a number: "))
# print(user)

# if user in num :
#     print("Yes")
# else:
#     print("No")

# elif statements
'''WAP to find greatest and smallest number'''

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# if a > b:
#     print("print a is greater than b")
# elif a < b:
#     print("a is smaller than b")
# elif a == b:
#     print("a and b are equal")
# if a >= b:
#     print("a is greater and equal to b")
# elif a <= b:
#     print("a is smaller and equal to b")
# else:
#     print("a and b is not equal")

# Nested if else

# result = int(input("Enter your marks: "))


# if result <= 30:
#     if result >= 30:
#         print("Just Pass")
#     else:
#         print("Failed")
# elif result >= 90:
#     print("A+")
# elif result >= 80:
#     print("B+")
# elif result > 50:
#     print("D")
# # else:
# #     print("Done")

""" WAP using module which greets you depending upon on time"""

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)

if hour >= 0 and hour < 12:
    print("Goodmorning Sir!")
elif hour >= 12 and hour < 17:
    print("GoodAfternoon Sir!")
elif hour >= 17 and hour < 0:
    print("GoodEvening Sir!")

