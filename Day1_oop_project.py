# lets create a mini project - contact manager with OOP ( its very simple )

class contact: 
    def __init__(self, name, phone):
        self.name = name 
        self.phone = phone
    
    def display(self):
        print(f"Name: {self.name} - Phone: {self.phone}")
        
name = input("Please enter your name: ")
phone = int(input("Please enter your phone number: "))

Contact = contact(name, phone)
Contact.display()