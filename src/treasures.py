from item import Item

class Treasure(Item):
    def __init__(self, name, description, price):
        super().__init__(name, description)
        self.price = price
    
    def __str__(self):
        output = super().__str__()
        output + f"This is worth ${self.price}"
        return output