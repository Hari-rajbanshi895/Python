# class Library():
    
#     def __init__(self):
#         self.noBooks = 0
#         self.books = []
    
#     def addbooks(self,book):
#         self.books.append(book)
#         self.noBooks = len(self.books)
    
#     def showinfo(self):
#         print(f"{self.books}")
    
#     def noofbooks(self):
#         print(f"{self.noBooks}")

# result = Library()
# result.addbooks("Python")
# result.addbooks("Java")
# result.addbooks("C++")
# result.addbooks("c#")
# result.showinfo()
# result.noofbooks()

    


class Person():
    def __init__(self,name,salary):
        self.name = name      
        self.salary = salary     
    @classmethod
    def fromstr(cls,string):
        return (string.split("-"[0],int(string.split("-")[1])))

p = Person("Hari",12000)
print(p.name,p.salary)

string = ("Himal-12000","Ronaldo-20000")
e1 = Person.fromstr(string)
print(e1)

name = "Sita-24000"
e2 = Person.fromstr(name)
print(e2)