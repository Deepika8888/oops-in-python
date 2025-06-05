# lets revise __str__ and learn about __repr__ 

class Book: 
    def __init__ (self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
           return f"{self.title} by {self.author}"
       
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')" #Used for developers/debugging – shows a more detailed/internal representation.
    
book = Book("I am a Cat", "Natsume Soseki")
print(book)
print(repr(book)) #repr gives a more detailed representation of the object. 
    

    
    