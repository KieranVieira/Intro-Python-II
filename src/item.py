class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}."

    def on_take(self):
        print(f"You have picked up {self.name}, you can drop it by specifying 'drop [ITEM NAME]")

    def on_drop(self):
        print(f"You have dropped {self.name}, you can drop it by specifying 'drop [ITEM NAME]")

class LightSource(Item):
    def on_drop(self):
        print("It's not wise to drop your source of light!")