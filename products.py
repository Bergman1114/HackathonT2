class Products:
    def __init__(self, id = None, make = None, year = None, model = None, color = None, price = None, status='A'):
        self.make = make
        self.year = year
        self.model = model
        self.color = color
        self.price = price
        self.status = status
        self.id = id
    
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
        self.price = price

    def getPrice(self):
        return self.price

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id