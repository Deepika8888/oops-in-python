#lets learn @classmethod 

class Person: 
    count = 0 #class variable, Keeps track of how many Person objects have been created
    
    def __init__(self,name):
        self.name = name
        Person.count +=1
    
    @classmethod  #A class method that accesses class-level data (like count)
    def get_count(cls):
        return cls.count
    
p1 = Person("Roshani")
p2 = Person("Anjal")
p3 = Person("Deepika")
p4 = Person("Niketa")
print(Person.get_count())