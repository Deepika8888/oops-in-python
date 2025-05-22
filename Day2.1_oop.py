#lets learn to use __str__() method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
       return f"{self.name}, Age: {self.age}"

    def can_vote(self):
        return self.age >= 18

person1 = Person("Roshani", 90)
print(person1)
# __str__() is used to define a readable string representation of the object.
# It lets us control what gets printed when we use print(obj).
