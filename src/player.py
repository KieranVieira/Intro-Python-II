# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom, items = []):
        self.name = name
        self.currentRoom = currentRoom
        self.items = items
        

    def moveRoom(self, direction):
        try:
            newRoom = getattr(self.currentRoom, direction)
            if newRoom:
                self.currentRoom = newRoom
                print(f'You have moved to the room {newRoom.name}\n')
                if not newRoom.is_light:
                    print("Its pitch black!")
            else:
                print("There is no room in that direction\n")
        except AttributeError:
            print("There is no room in that direction\n")

    def getItem(self, item):
        added = False
        if self.currentRoom.items: 
            for index, element in enumerate(self.currentRoom.items):
                if element.name.lower() == item.lower():
                    element.on_take()
                    self.items.append(self.currentRoom.items[index])
                    self.currentRoom.removeItem(self.currentRoom.items[index])
                    added = True

        if not added:
            print("That item is not in the room\n")

    def dropItem(self, item):
        removed = False
        for index, element in enumerate(self.items):
            if element.name.lower() == item.lower():
                element.on_drop()
                self.items.remove(self.items[index])
                removed = True
                self.currentRoom.addItem(element)

        if not removed:
            print("That item is not in your inventory")