from room import Room
from player import Player
from item import Item, LightSource
from treasures import Treasure

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [LightSource("Lamp", "Plain old lamp")], is_light=True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", is_light=True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", is_light=False),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", is_light=False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [
    Item("Sword", "Just a plain old sword, nothing special"), 
    Treasure("Gold", "A chest of the finest gold you have ever seen.", 4560345),
], is_light=False),
    'off the cliff': Room("A pitiful fall", """You ran so fast off the cliff, you fall into it and die.""", [Item("Bones", "Lots of bones from past travelers")], is_light=True)
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['overlook'].n_to = room['off the cliff']

#
# Main
#

player = Player("Kieran", room['outside'])

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

gameActive = True

while gameActive:
    if player.currentRoom.is_light:
        print(f"Room description: \n{player.currentRoom}\n")
        if player.currentRoom.items:
            print(f"The following items are in the room. You can grab them by specifying 'get [ITEM NAME]':")
            for i in player.currentRoom.items:
                print(i.name)
    else:
        print("You can't see anything")
    userInput = input("Select a direction of 'n', 'e', 's', 'w', or 'q' to quit:")
    print("\n")
    if len(userInput.split()) == 1:
        if userInput == "n" :
            print("You try to move to the North.\n")
            player.moveRoom("n_to")
        elif userInput == "e" :
            print("You try to move to the East.\n")
            player.moveRoom("e_to")
        elif userInput == "s" :
            print("You try to move to the South.\n")
            player.moveRoom("s_to")
        elif userInput == "w" :      
            print("You try to move to the West.\n")
            player.moveRoom("w_to")
        elif userInput == "q":
            print("Game has been quit\n")
            gameActive = False
        elif userInput == "i" or userInput == "inventory":
            if player.items: 
                output = "You have the following items in your inventory:"
                for i in player.items:
                    output += f" {i.name}"
                print(output)
            else:
                print("You have no items in your inventory")
        else:
            print("Please enter a valid direction.")
    elif len(userInput.split()) > 1:
        if "get" in userInput:
            player.getItem(str.split(userInput)[1])
        if "drop" in userInput:
            player.dropItem(str.split(userInput)[1])
    else:
        print("Please enter a valid query.")

        # isinstance 

def unique_in_order(iterable):
    outputArr = []
    prevItem = ""
    for i in iterable:
        if prevItem != i:
            outputArr.append(i)
        prevItem = i