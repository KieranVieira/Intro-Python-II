# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None, is_light=False):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.is_light = is_light

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