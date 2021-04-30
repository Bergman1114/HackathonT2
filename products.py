class Products:
    def __init__(self,make = None, year = None, model = None, color = None):
        self.make = make
        self.year = year
        self.model = model
        self.color = color
    
    def setMake(self, make):
        self.make = make

    def getMake(self):
        return self.make

    def setYear(self, year):
        self.year = year

    def getYear(self):
        return self.year

    def setModel(self, model):
        self.model = model

    def getModel(self):
        return self.model

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPrice(self, price):
        self.color = color

    def getPrice(self):
        return self.price