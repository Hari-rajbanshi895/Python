'''~~~ Match Case ~~~'''

num = int(input("Enter a number: "))

match num:
    case 0:
        print("num is zero")

    case 1:
        print("num is 1")

    case _:
        print(num)
    