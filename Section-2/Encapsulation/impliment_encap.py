class Student:
    def setId(self,id):
        self.id = id

    def getId(self):
        print(self.id)

    def setName(self,name):
        self.name = name

    def getName(self):
        print(self.name)


s = Student()
s.setId(1)
s.setName("Johny")
s.getId()
s.getName()