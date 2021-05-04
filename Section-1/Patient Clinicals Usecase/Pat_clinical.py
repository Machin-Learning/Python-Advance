class Patient:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.clinical = []
    
    def addClinical(self,clinical):
        self.clinical.append(clinical)

class Clinical:
    def __init__(self,clinicalCompName,clinicalCompValue):
        self.clinicalCompName = clinicalCompName
        self.clinicalCompValue = clinicalCompValue

p1 = Patient("JOHN", 26)
c1 = Clinical("BP", "80/120")
p1.addClinical(c1)

c2 = Clinical("heartRate", 80)
p1.addClinical(c2)
print(p1.name)
for eachClincals in p1.clinical:
    print(eachClincals.clinicalCompName)
    print(eachClincals.clinicalCompValue)