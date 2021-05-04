class ObjectCounter:
    numOfObjects = 0
    def __init__(self):
        ObjectCounter.numOfObjects +=1

    def displayCount():
        print(ObjectCounter.numOfObjects)



o1 = ObjectCounter()
o2 = ObjectCounter()
o3 =ObjectCounter()
ObjectCounter.displayCount()
