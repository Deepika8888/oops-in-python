#mini project : student management system 
class Student: 
    def __init__ (self, name, grade):
        self.name = name
        self.__grade = grade #private attribute
        
    @property 
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self,value):
        if value <0 or value>100:
            self._grade = value
        else: 
            print("Invalid grade.")
    
    def __str__(self):
        return f"Student: {self.name}, Grade: {self.__grade}"
    
student1 = Student("Roshani",85)
print(student1)
student1.grade = 95 #updating using setter
print(student1)