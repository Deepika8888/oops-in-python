#lets learn some more @property 

class Temperature: 
    def __init__(self, celsius):
        self.__celsius = celsius 
        
    @property 
    def fahrenheit(self):
        return(self.__celsius *9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.__celsius = (value - 32) * 5/9 
        
temp = Temperature(0)
print(temp.fahrenheit)  
temp.fahrenheit = 212
print(temp.fahrenheit) 