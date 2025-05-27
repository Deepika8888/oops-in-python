#lets learn about class vs instance attributes

class Dog: 
    species = 'canines' #class attribute, shared by all instances
    def __init__(self, name):
        self.name = name #instance attribute, unique to each instance
        
    
dog1 = Dog("Buddy")
dog2 = Dog("julie")

print(dog1.name)
print(dog2.name)
print(dog1.species)
        