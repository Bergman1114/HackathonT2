class CarDetail:
    def __init__(self, carPrice = None, dnpaymentAmount = None, notes = None, disc_amount = None, final_price = None, tax_amount = None, bonus = None):
        self.carPrice = carPrice
        self.dnpaymentAmount = dnpaymentAmount
        self.notes = notes
        self.disc_amount = disc_amount
        self.final_price = final_price
        self.tax_amount = tax_amount
        self.bonus = bonus
    
    
    def setCarPrice(self, carPrice):
        self.carPrice = carPrice

    def getCarPrice(self):
        return self.carPrice

    
    def setDnpaymentAmount(self, dnpaymentAmount):
        self.dnpaymentAmount = dnpaymentAmount

    def getDnpaymentAmount(self):
        return self.dnpaymentAmount

            
    def setNotes(self, notes):
        self.notes = notes

    def getNotes(self):
        return self.notes

            
    def setDisc_amount(self, disc_amount):
        self.disc_amount = disc_amount

    def getDisc_amount(self):
        return self.disc_amount

            
    def setFinal_price(self, final_price):
        self.final_price = final_price

    def getFinal_price(self):
        return self.final_price

            
    def setTax_amount(self, tax_amount):
        self.tax_amount = tax_amount

    def getTax_amount(self):
        return self.tax_amount

    def setBonus(self, bonus):
        self.bonus = bonus

    def getBonus(self):
        return self.bonus
        
