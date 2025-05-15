""" Generators in Python """
def generator():
    for i in range(500000):
        yield i
a = generator()
print(next(a))
print(next(a))
print(next(a))
print(next(a))