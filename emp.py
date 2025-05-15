class Employee:
    def __init__(self,id):
        self.name = "Himal"
        self.id = id

    def __str__(self):
        return f"My name is {self.name} str"
    
    def __repr__(self):
        return f"My name is {self.name} repr"
    
    def __call__(self):
        return self.id