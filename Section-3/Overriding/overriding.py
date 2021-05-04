# Inheritance can be define as the process where one class acquires the properties (method and fields) of another.
# With the use of inheritance the information is made manageable in a hierarchical order.

class BMW:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print("Strating a Car")

    def stop(self):
        print("Stoping the Car")
    
class ThreeSeries(BMW):
    def __init__(self,cruisecontrolEnabled,make,model,year):
        BMW.__init__(self, make, model, year)
        self.cruisecontrolEnabled = cruisecontrolEnabled

    def display(self):
        print(self.cruisecontrolEnabled)

    def start(self):
        print("Button Start")

class FiveSeries(BMW):
    def __init__(self,parkingAssistEnabled,make,model,year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled


threeSeries = ThreeSeries(True, "BMW", "328i", 2018)
print(threeSeries.cruisecontrolEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()