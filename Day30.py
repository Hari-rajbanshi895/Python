# Inheritance in python 
# Single level inheritance

# class Animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species  = species

#     def makesound(self):
#         print("Animal make sound")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self,name, species ="Dog")
#         self.breed = breed

#     def makesound(self):
#         print("Bark!")

# d = Dog("Dog","gorey")
# print(d.makesound())

# a = Animal("Dog","Dog")
# print(a.makesound())

# Multiple inheritance/ hybrid inhericance
class Employee:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"name: {self.name}")

class Dance:
    def __init__(self,dance):
        self.dance = dance

    def show(self):
        print(f"dance: {self.dance}")

class DanceEmployee(Employee,Dance):
    def __init__(self,name,dance):
        self.name = name
        self.dance = dance

o = DanceEmployee("Hiphop","Micheal")
print(o.show())

# multilevel inheritance

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def showdetails(self):
        print(f'name: {self.name}')
        print(f'species: {self.species}')

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed

    def showdetails(self):
        Animal.showdetails(self)
        print(f'breed: {self.breed}')
    
class GoldenRetriver(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="Golden Retriver")
        self.color = color

    def showdetails(self):
        Dog.showdetails(self)
        print(f'color: {self.color}')

o = GoldenRetriver("Hridesh","Black")
print(o.showdetails())

# Hierarchical inherittance

class Shops:
    def __init__(self,name,product):
        self.name = name
        self.product = product

    def show(self):
        print(f'name: {self.name}')
        print(f'product: {self.product}')

class MilkTea(Shops):
    def __init__(self,name,owner):
        Shops.__init__(self,name,product="Chai lelo")
        self.owner = owner

    def show(self):
        Shops.show(self)
        print(f'owner: {self.owner}')

class Variety(MilkTea):
    def __init__(self, name, variety):
        MilkTea.__init__(self,name,owner="Hridesh")
        self.variety = variety

    def show(self):
        MilkTea.show(self)
        print(f'Variety: {self.variety}')

class Kirana(Shops):
    def __init__(self,name,owner):
        Shops.__init__(self,name,product="Ganja")
        self.owner = owner

    def show(self):
        Shops.show(self)
        print(f'owner: {self.owner}')



p = Variety("HD Chai Pasal","five")
print(p.show())

q = Kirana("HD Ganja Interprise.CO", "Hridesh")
print(q.show())