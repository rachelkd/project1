"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
from game_data import World, Item, Location, Player, Furniture

# Note: You may add helper functions, classes, etc. here as needed

if __name__ == "__main__":
    w = World(open("map.txt"), open("locations.txt"), open("items.txt"))
    p = Player(2, 4, w)  # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit", "back"]

    # TODO: Make World method. Make sure to include menu in intro
    print(w.get_game_introduction())
    input('Press ENTER to continue.')

    while not p.victory:
        location = w.get_location(p.x, p.y)

        # Print location description depending on if player has visited before
        location.visit()
        available_actions = location.get_available_actions()

        print("What to do? \n")
        choice = input("\nEnter action: ").lower()

        if choice == "menu":
            print("Menu Options: \n")
            for option in menu:
                print(option)
            print(f'\nActions available at LOCATION {location.num}: \n')
            for action in available_actions:
                print(f'{action} [Additional argument, if applicable]')
                # Print all Item or Furniture objects that an action can be performed on.
                print('\t' + '\t'.join(available_actions[action]))
            choice = input("\nChoose action: ")

        # TODO: CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON THE PLAYER'S CHOICE
        #  REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if
        #  the choice the player made was just a movement, so only updating player's position is enough to change the
        #  location to the next appropriate location
        #  Possibilities:
        #  A helper function such as do_action(w, p, location, choice)
        #  OR A method in World class w.do_action(p, location, choice)
        #  OR Check what type of action it is, then modify only player or location accordingly
        #  OR Method in Player class for move or updating inventory
        #  OR Method in Location class for updating location item info, or other location data etc....
