# finally keyword in python



def func1():
    try:
        l = [1,3,7,9]
        i = int(input('Enter an index: '))
        print(l[i])
        # return 1

    except:
        print("Invalid input")
        # return 0

    finally:
        print('Im always executed')

x = func1
print(func1)

# try:
#     l = [1,3,7,9]
#     i = int(input('Enter an index: '))
#     print(l[i])
    

# except:
#     print("Invalid input")
#     # return 0

# # finally:
#     print('Im always executed')