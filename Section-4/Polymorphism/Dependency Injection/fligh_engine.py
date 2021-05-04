class Flight:
    def __init__(self,engine):
        self.engine =engine

    def startEngine(self):
        self.engine.start()


class AirbusEngine:
    def start(self):
        print("Starting Airbus Engine")

class BoingEngine:
    def start(self):
        print("Starting Boing Engine")


ae = AirbusEngine()
f = Flight(ae)
be = BoingEngine()
f1 = Flight(be)

f.startEngine()
f1.startEngine()