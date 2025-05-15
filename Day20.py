# Global variable and local variable:

# x = 5

# def calculate():
#     x = 4
#     print(f"This is local variable {x}")

# print(calculate())
# print(f"This is global variable {x}")

x = 5

def calculate():
    global x
    print(f"This is local variable {x}")

print(calculate())
print(f"This is global variable {x}")
