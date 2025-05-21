# let's learn to define a simple class 

class person:
    def __init__(self, name, age): #constructor method
        self.name = name #instance variable
        self.age = age #instance variable

    def greet(self): #method that uses the instance variables. 
        print(f"My name is {self.name} and I am {self.age} years old.")
        

#lets create an object from the class

person1 = person("Deepika", 80)
person2= person("jonny", 90)
person1.greet() #calling the method of the class using the object. 
person2.greet()