#lets create a mini project to understand better

class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def greet(self):
        print(f"Hello, my name is {self.name}, and I am {self.age} years old.")
        
    def can_vote(self):
        return self.age >= 18
    
    def __str__(self):
        return f"{self.name} (Age: {self.age})"
    
#let's take input

name = input("Enter your name: ")
age = int(input("Enter your age: "))

user = Person(name, age) 
print(user)

#user.greet()
#print(f"Can vote? {'Yes' if user.can_vote() else 'No'}")
#print("User info:", user)