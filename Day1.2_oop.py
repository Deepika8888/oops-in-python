#another similar program

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"The dog name is {self.name} and the breed is {self.breed}")
  
dog_ask = (input("Please enter your name doggie: ")) 
dog_ask2 = (input("Please enter your breed: "))
  
#creating object 
dog = Dog(dog_ask, dog_ask2)
dog.bark()