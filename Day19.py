# Enumerate function in python

# num = [1,23,34,556,76,7,87,2]

# index = 0
# for marks in num:
#     print(marks)
#     if(index == 3):
#         print("Well done!!")
#     index += 1

# num = [1,23,34,556,76,7,87,2]


# for index,marks in enumerate(num):
#     print(marks)
#     if(index == 3):
#         print("Well done!!")

fruits = ["apple","banana","grapes","mango"]

for index, i in enumerate(fruits,start=1):
    print(i)
    if(index == 2):
        print("Litchi")

