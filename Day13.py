# Exceptional Handeling in python

a = input("Enter a number: ")

try:
    print(f"Multiplication table of {a} is")
    for i in range (1,11):
        print(f'{int(a)} X {i} = {int(a)*i} ')
except Exception as e:
    print(e)