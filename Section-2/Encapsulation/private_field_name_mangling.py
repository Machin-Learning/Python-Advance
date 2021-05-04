# Encapsulation is a mechanism of wrapping the data(Variable) and code(method) together as a single unit.

class Student:
    def __init__(self,id,name):
        self.__id = id   #private variable/data
        self.__name = name  #private variable/data

    def display(self):
        print(self.__id)
        print(self.__name)


s = Student(1, "Johny")
# print(s.id)  #AttributeError: 'Student' object has no attribute 'id'
# print(s.name) #AttributeError: 'Student' object has no attribute 'name'
s.display()

#Name mangling
print(s.__dict__)  #-->{'_Student__id': 1, '_Student__name': 'Johny'}
print(s._Student__id)
print(s._Student__name)
