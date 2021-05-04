# Inheritance can be define as the process where one class acquires the properties (method and fields) of another.
# With the use of inheritance the information is made manageable in a hierarchical order.

# Interface is nothing but all the method are abstract
from abc import abstractmethod,ABC

class BMW(ABC):
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    @abstractmethod
    def start(self):
        print("Strating a Car")

    @abstractmethod
    def stop(self):
        print("Stoping the Car")

    @abstractmethod
    def drive(self):
        pass
    
class ThreeSeries(BMW):
    def __init__(self,cruisecontrolEnabled,make,model,year):
        super().__init__(make, model, year)
        self.cruisecontrolEnabled = cruisecontrolEnabled

    def display(self):
        print(self.cruisecontrolEnabled)

    def start(self):
        super().start()
        print("Button Start")

    def stop(self):
        super().stop()
        print("Button Stop")

    def drive(self):
        print("Three Series is being driven")


class FiveSeries(BMW):
    def __init__(self,parkingAssistEnabled,make,model,year):
        super().__init__( make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def start(self):
        super().start()
        print("Remote Start")

    def stop(self):
        super().stop()
        print("Remote Stop")

    def drive(self):
        print("Five Series is being driven")


threeSeries = ThreeSeries(True, "BMW", "328i", 2018)
print(threeSeries.cruisecontrolEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()
threeSeries.drive()

fiveSeries = FiveSeries(True, "BMW", "328i+", 2022)