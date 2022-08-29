class Vehichle:
    def __init__(self,name=str,mileage=str,capacity= int, color=str, no_of_passagers = int, price_for_each= int):
        self.name = name 
        self.mileage = mileage 
        self.capacity = capacity
        self.tyres = 4
        self.color = color
        self.no_of_passagers = no_of_passagers
        self.price_for_each = price_for_each
        
    def addPassager(self, new_passager = int):
        self.no_of_passagers = new_passager + self.no_of_passagers
        return self.no_of_passagers
        
    def removePassage(self,remove_passagers):
        self.no_of_passagers = self.no_of_passagers - remove_passagers
        return self.no_of_passagers
        
    def totalPassager(self):
        return self.no_of_passagers
    
    def totalFare(self):
        self.price_for_each = self.no_of_passagers * self.price_for_each
        
        
class Lexus(Vehichle):
    pass


class Toyato(Vehichle):
    pass


class Honda(Vehichle):
    pass


class Hyundia(Vehichle):
    pass


class Nissan(Vehichle):
    pass


class Audi(Vehichle):
    pass


class Bezn(Vehichle):
    pass
# v1 = Lexcus("Lexus", "150 mile/hr", 4)
# print(v1.mileage)