from room import Room
from player import Player
from item import Item

class Adventure:

item = {
    'flashlight': Item("Flashlight", "Great for seeing in a dark cave!"),
    'red_marker': Item("Red Marker", "To create a path if you lose your path...?"),
    'rope': Item("Rope", "For going down the steep cliff."),
    'metal_detector': Item("Metal Detector", "For finding the burried treasure! arg..."),
    'report_card': Item("Your Report Card", "A+ for trying...")
}

# DICTIONARY
rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     item["flashlight"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item["red_marker"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item["rope"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item["metal_detector"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item["report_card"]),
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

#Main

# 1. Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

# Make a new player object that is currently in the 'outside' room.
player_name = input("\nWelcome to the Adventure Game! Enter your name: ")
new_player = Player(player_name, room['outside'])
print(f"Welcome, {new_player.name}.\n")
print(f"{new_player.current_room.description}.\033[0,33m \n")
# Write a loop that:

directions = ["n", "N", "s", "S", "e", "E", "w", "W"]
while True:
    userInput = input(" Enter the direction you wish to go. If you want to quit, Enter Q to quit ---> ")
    if direction in directions:
        player.move(direction)
    elif direction in ["q", "Q"]:
        print("Better luck next time!")
        break
    else:
        print("Sorry! Invalid direction! try Again!\n")
