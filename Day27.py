# Inheritence in python 

# class employee():
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def empdetail(self):
#         print(f"The name of {self.id} is {self.name}")

# class programmer(employee):
#     def defaultlan(self):
#         print("My default language is python")

# obj = employee("himal rajbanshi",1)
# obj1 = programmer("hari",2)
# obj.empdetail()
# obj1.empdetail()
# obj1.defaultlan()

# Access Modifiers in Python
# Public access modifiers

# class School():
#     school_name = "Angelica Academy" # Class Variable
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno

#     def ShowDetails(self):
#         print(f"The student {self.name} is a student of {self.school_name} and his rollno is {self.rollno}")

#     @staticmethod # Static Method
#     def add(a,b):
#         print(a+b)
    
# stud1 = School("hari",2)
# School.school_name = "Google"
# stud1.ShowDetails()
# stud1.add(1,2)

# stud2 = School("Rabin",2)
# stud2.school_name = "Ganeshman"
# stud2.ShowDetails()
# stud2.add(5,6)

# Private access modifiers

class Shop():
    def __init__(self):
        self.__name = "Bookstore"
        self.__product = "Python"

c1 = Shop()
print(c1._Shop__name)
print(c1._Shop__product)

class Subject():
    def __init__(self):
        self.__name = "Science"

class Student(Subject):
    def __init__(self):
        self.__name = "Computer" # __name == Private access modifier

s1 = Subject()
s2 = Student()
print(s1._Subject__name)
print(s2._Student__name)

# Protected access modifiers

# class Tests():
#     def __init__(self,name,rollno,result):
#         self.name = name
#         self.rollno = rollno
#         self._result = result

#     def _show(self): # protected method
#         print(f"{self.rollno}   {self.name}   {self._result}")

# a = Tests("hari",1,"pass")
# print(a._result)
# a._show()

class Employee():
    def __init__(self):
        self._name = "hari"

    def _shows(self): # protected method
        return "Welcome Hari"

class Agent(Employee):
    pass

obj1 = Employee()
obj2 = Agent()

print(obj1._name)
print(obj2._shows())



# Class methods as alternative constructer

# class Person():
#     def __init__(self,name,salary):
#         self.name = name      
#         self.salary = salary     
#     @classmethod
#     def fromstr(cls,string):
#         return (string.split("-"[0],int(string.split("-")[1])))

# p = Person("Hari",12000)
# print(p.name,p.salary)

# string = ("Himal-12000")
# e1 = Person.fromstr(string)
# print(e1)

# name = "Sita-24000"
# e2 = Person.fromstr(name)
# print(e2)