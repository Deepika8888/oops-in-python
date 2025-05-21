#self practice 

class Age:
    def __init__(self, age):
        self.age = age
    def greet(self):
        if self.age >= 18:
            print(f"age is {self.age}")
        else:
            exit()
        

Age1 = int(input("Please enter your age: ")) #asking for a input

#create object 
person = Age(Age1)
person.greet()