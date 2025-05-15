# dir,dict and help method in python

# class Employee():
#     name = "Himal"
#     age = 12
#     male = True

# e1 = Employee()
# print(e1.name,e1.age,e1.male)
# # print(dir())
# print(Employee.__dict__)
# print(help())

# a = [1,23,43]
# print(help())

# Super Keyword in Python:

class ParentClass:
    def parent_method(self):
        print("This is a Parent class")

class ChildClass(ParentClass):
    def parent_method(self):
        return "hari"
        
    
    def child_method(self):
        print("This is Child method")
    
child_obj = ChildClass()
child_obj.child_method()
child_obj.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        self.lang = lang
        super().__init__(name, id)

obj = Employee("Sita", 102)
obj1 = Programmer("Hari", 101, "Python")
print(obj1.name)
print(obj1.id)
print(obj1.lang)