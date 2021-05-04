class Programmer:
    def setName(self,name):
        self.name = name
    
    def setSalary(self,sal):
        self.salary = sal

    def setTechnologies(self,Techs):
        self.technologies = Techs

    def getName(self):
        return self.name

    def getSalarty(self):
        return self.salary

    def getTechnologies(self):
        return self.technologies



p1 = Programmer()

p1.setName("Muzmmil")
p1.setSalary(10000)
p1.setTechnologies(["Java","Python","ML","AI"])

print(p1.getName())
print(p1.getSalarty())
print(p1.getTechnologies())