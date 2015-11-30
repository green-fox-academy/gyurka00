class Car:
    def __init__(self,color,type,km):
        self.color = color
        self.type = type
        self.km = km

    def ride(self, km):
        self.km += km


tesla = Car ('pink','Tesla S',1200)

tesla.ride(220)

print(tesla.km)
