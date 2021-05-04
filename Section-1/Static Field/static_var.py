class Student:
    major = "ECE"
    def __init__(self,rollnum,name):
        self.rollnum = rollnum
        self.name = name


s1 = Student(1, "Muzmmil")
s2 = Student(2, "khalid")
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)

print(Student.major)