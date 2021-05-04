from threading import *

class BookMyTicket:
    def __init__(self,avalableSeats):
        self.avalableSeats = avalableSeats
        self.l = Lock()
    def buy(self,SeatsRequested):
        self.l.acquire()
        print("Avalable Seats:",self.avalableSeats)
        if self.avalableSeats >= SeatsRequested:        
            print("Conforming a Seat")
            print("Processing the payment")
            print("Booking a Ticket")
            self.avalableSeats -= SeatsRequested
        else:
            print("Sorry! No seats avalable")
        self.l.release()

myticket = BookMyTicket(10)

t1 = Thread(target=myticket.buy,args=(3,))
t1.start()
t2 = Thread(target=myticket.buy,args=(4,))
t2.start()
t3 = Thread(target=myticket.buy,args=(4,))
t3.start()