class Car:
    def __init__(self,make,year):
        self.make = make
        self.year = year

    class Engine:
        def __init__(self,numbers):
            self.numbers = numbers

        def start(self):
            print("Engine Started")



c = Car("BMW", 2021)

e = c.Engine(4)

e.start()