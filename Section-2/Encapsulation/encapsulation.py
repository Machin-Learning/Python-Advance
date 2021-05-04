# Encapsulation is a mechanism of wrapping the data(Variable) and code(method) together as a single unit.

class Student:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def display(self):
        print(self.id)
        print(self.name)


s = Student(1, "Johny")
print(s.id)
print(s.name)