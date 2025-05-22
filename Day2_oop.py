#let's learm to create a class with multiple attributes and methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def can_vote(self):
        return self.age>= 18
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
#creating multiple objects. 

person1= Person("Roshani", 17)
person2 = Person("Niketa", 70)

person1.greet()
person2.greet()
    
#lets use logic in a method

print(f"Can {person1.name} vote? {'Yes' if person1.can_vote() else 'No'}")
print(f"Can {person2.name} vote? {'Yes' if person2.can_vote() else 'No'}")
