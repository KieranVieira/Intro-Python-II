# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f"This is the {self.name} room. \n {self.description}"

    def removeItem(self, item):
        if self.items:
            self.items.remove(item)

    def addItem(self, item):
        if not self.items:
            self.items = [item]
        else:
            self.items.append(item)