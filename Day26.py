# {OOP} Object oriented programming in python

class person():
    name = "himal"
    occupation = "backend web developer"
    age = 22

a = person()
b = person()
a.name = "hari"
a.occupation = "HR"
b.name = "sita"
b.occupation = "intern"

print(f"{a.name} is a {a.occupation} and his age is {a.age}")

# Constructer

class shop():
    def __init__(self):
        self.name = "hridesh dhungana"   # Parameterized constructer
        self.location = "shivasatakshi"
        self.type = "kirana"

    def show(self):
        print(f"The shopkeeper name is {self.name} and he lives in {self.location} and he wons {self.type} shop")


a = shop()
b = shop()
c = shop()
c.show()
b.name = "sita"
b.location = "Bhaktapur"
b.type = "Bakery"
b.show()
a.name = "Hari Rajbanshi"
a.location = "kathmandu"
a.type = "It institute"
a.show()

class fruits():  
    def __init__(self):   # Default constructors
        print(f"Hi i am a constructor")

a = fruits()

# Decorator

def greet(fx):
    def mfx(*args,**kwargs):
        print('Good Morning!')
        fx(*args,**kwargs)
        print("Thanks For visiting")
    return mfx

@greet
def hello():
    print("Hello hari!,good afternoon!")
@greet
def multiply(a,b):
    print(a*b)

hello()
multiply(8,9)
        
# Getter

class add():
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"The value is {self._value}")

    @property
    def ten_value(self):
        return 10* self._value
    
    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10
        
    
a = add(50)
a.ten_value = (100)
print(a.ten_value)
a.show()

