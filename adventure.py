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


    action_input = player_input[0]
    arg = ' '.join(player_input[1:])
    if action_input == 'go':
        if arg == 'north':
        elif arg == 'south':
            w.move_player(p.x, p.y + 1, p)
        elif arg == 'east':
            w.move_player(p.x + 1, p.y, p)
        elif arg == 'west':
            w.move_player(p.x - 1, p.y, p)
        else:
            print('\nInvalid direction. Please go north, east, south, or west.')
    elif action_input == 'pick':
    elif action_input == 'drop':
<<<<<<< Updated upstream
        w.drop(p, location, arg)
    elif action_input == 'look':
        location.get_long()
        world.drop(player, player_location, arg)

    else:


if __name__ == "__main__":
    w = World(open("map.txt"), open("locations.txt"), open("items.txt"))
    p = Player(2, 4, w)  # set starting location of player; you may change the x, y coordinates here as appropriate
    w.add_interactables_to_locations()
    w.add_actions_to_locations()

    menu = ["go", "look", "inventory", "score", "quit"]

    w.get_game_introduction()
    input('Press ENTER to continue.')

    while not p.victory:
        location = w.get_location(p.x, p.y)

        # Print location description depending on if player has visited before
        location.visit()
        available_actions = location.available_actions

        print("What to do?\n")
        choice = input("\nEnter action: ").lower()

        if choice == "menu":
            print("Menu Options: \n")
            for option in menu:
                print(option)
            print(f'\nActions available at LOCATION {location.num}: \n')
            for action in available_actions:
                print(f'{action} [argument]')
                # Print all Item or Furniture objects that an action can be performed on.
                print('\t' + ', '.join(available_actions[action]) + '\n')

        do_action(w, p, location, choice)

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


def check_for_victory(p: Player) -> bool:
    """
    Checks for victory xd
    """
    at_exam_hall = (p.y == 4) and (p.x == 3)
    has_all_items = [False, False, False]

    for item in p.inventory:
        if item.name == 'tcard':
            has_all_items[0] = True
        if item.name == 'cheat sheet':
            has_all_items[1] = True
        if item.name == 'lucky pen':
            has_all_items[2] = True

    if at_exam_hall and (all(status for status in has_all_items)) and p.moves < 60:
        return True
    else:
        return False
