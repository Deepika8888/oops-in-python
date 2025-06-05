# lets creare a mini student database with oop 

class Student: 
    total_students = 0
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.total_students += 1
    
    @classmethod
    def get_total(cls):
       return cls.total_students
  
    @staticmethod
    def is_passing(grade):
        return grade >= 60

    def __str__(self):
        return f"{self.name} - Grade: {self.grade} ({'Pass' if self.is_passing(self.grade) else 'Fail'})"
    
s1 = Student("Roshani", 85)
s2 = Student("Niketa", 70)
s3 = Student("Anjal", 40)

print(s1)
print(s2)
print("Total students:", Student.get_total()) 