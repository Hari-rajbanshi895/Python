# Method overiding in python

# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.x * self.y
    
# class Circle(Shape):   # Only works in inherited class 
#     def __init__(self,radius):
#         self.radius = radius
#         super().__init__(radius,radius) # Overriding Parent method


#     def area(self):
#         return 3.14 * super().area()
    

# rect = Shape(3,5)
# print(rect.area())

# result = Circle(5)
# print(result.area())

# class Animal:
#     def speak(self):
#         print("Animals Speak")

# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print("Dog Barks")

# wild = Animal()
# print(wild.speak())

# dog = Dog()
# print(dog.speak())

# Operator overriding in python

class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f'{self.i}i + {self.j}j + {self.k}k'
    
    def __add__(self,x):
        return Vector(self.i + x.i, self.j + x.j , self.k + x.k)
    
v1 = Vector(2,4,5)
print(v1)

v2 = Vector(2,4,5)
print(v2)

print(v1 + v2)
print(type(v1 + v2))