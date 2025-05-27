#lets learn about @propert and setter

class Temperature: 
    def __init__(self, celsius):
        self.__celsius = celsius
        
    @property #@property allows method access like an attribute.
    def fahrenheit(self):
        return (self.__celsius *9/5) +32
    
    @fahrenheit.setter #@setter allows setting the value of the property. 
    def fahrenheit(self, value):
        self.__celsius = (value - 32) * 5/9
    
temp = Temperature(0)
print(temp.fahrenheit)  
   
temp.fahrenheit = 100
print(temp.fahrenheit) 