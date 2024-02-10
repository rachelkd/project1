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
from game_data import World, Item, Location, Player, MissionLocation

# Note: You may add helper functions, classes, etc. here as needed


def do_action(world: World,
              player: Player,
              player_location: Location,
              player_choice: str,
              menu_actions: list[str]) -> None:
    """
    Handles an action that a player executes in a given world based on player input.
    If action is not a move function, then it prompts player for another action, and recursively calls this function.
    Returns 1 if player quits.
    """

    try:
        action_input = player_choice.lower().split()[0]
    except IndexError:
        action_input = ''
    arg = ' '.join(player_choice.lower().split()[1:])

    if action_input == 'go':
        if arg == 'north':
            world.move_player(player.x, player.y - 1, player)
            # return
        elif arg == 'south':
            world.move_player(player.x, player.y + 1, player)
            # return
        elif arg == 'east':
            world.move_player(player.x + 1, player.y, player)
            # return
        elif arg == 'west':
            world.move_player(player.x - 1, player.y, player)
            # return
        else:
            print('\nInvalid direction. Please go north, east, south, or west.')
    elif action_input == 'pick':
        world.pick(player, player_location, arg)
    elif action_input == 'drop':
        world.drop(player, player_location, arg)
    elif action_input == 'look':
        player_location.get_long()
    elif action_input == 'quit':
        # return
        pass
    elif action_input == 'score':
        print(f'Score: {player.score}')
    elif action_input == 'inventory':
        inv = []
        for item in player.inventory:
            inv.append(item.name)
        if not inv:
            print('Inventory is empty.')
        else:
            print(', '.join(inv))
    elif action_input == 'open':
        if 'open' not in player_location.available_actions:
            print('Nothing can be opened in this location.')
        elif arg in player_location.available_actions['open']:
            world.open(player, player_location, arg)
        else:
            print(f'You cannot open a {arg}.')

    elif action_input == 'menu':
        print("Menu Options: \n")
        for option in menu_actions:
            print(option)
        print(f'\nActions available at LOCATION {player_location.num}: \n')
        for action in player_location.available_actions:
            print(f'{action} [argument]')
            # Print all Item or Furniture objects that an action can be performed on.
            print('\t' + ', '.join(player_location.available_actions[action]) + '\n')
    elif (any(action_input == a for a in player_location.available_actions)
          or any(action_input == a for i in p.inventory for a in i.actions)):
        obj = None
        # Check if item is in inventory
        if arg in {i.name for i in player.inventory}:
            for item in player.inventory:
                if item.name == arg:
                    obj = item
                    break
        # Check if interactable is in location
        else:
            for interactable in player_location.interactables:
                if interactable.name == arg:
                    obj = interactable
                    break
        if obj:
            if isinstance(obj, Item):
                if action_input in obj.actions:
                    obj.do_action(player, action_input)
                else:
                    print('You cannot do that action on this object.')
            else:
                if action_input in obj.actions:
                    obj.do_action(world, player, player_location, action_input)
                else:
                    print('You cannot do that action on this object.')
        else:
            print(f'{arg} does not exist in your inventory or at this location.')
    else:
        print('Invalid action.')

    # Prompt player for action again
    # player_choice = input("\nChoose action: ")
    # call = do_action(world, player, player_location, player_choice, menu_actions)
    # Check if player called quit

    # return


def check_for_victory(player: Player) -> bool:
    """
    Returns True if the given player has won.
    A player has won if they are at the exam center with a tcard, cheat sheet, and lucky pen in their inventory
    """
    at_exam_hall = (player.y == 4) and (player.x == 3)
    has_all_items = [False, False, False]

    for item in player.inventory:
        if item.name == 'tcard':
            has_all_items[0] = True
        if item.name == 'cheat sheet':
            has_all_items[1] = True
        if item.name == 'lucky pen':
            has_all_items[2] = True

    if at_exam_hall and (all(status for status in has_all_items)) and player.moves < 60:
        return True
    else:
        return False


if __name__ == "__main__":
    quit_game = False

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120
    })

    with open("map.txt") as map_file, open("locations.txt") as locations_file, open("items.txt") as items_file:
        w = World(map_file, locations_file, items_file)

        p = Player(2, 4, w)  # set starting location of player; you may change the x, y coordinates here as appropriate
        w.add_interactables_to_locations()
        w.add_actions_to_locations()

        menu = ["go", "look", "inventory", "score", "quit"]

        w.get_game_introduction()
        print(f'You can always type {', '.join(menu)} at any location.\n')
        input('Press ENTER to continue.')

        while not p.victory and p.moves < 60 and not quit_game:
            location = w.get_location(p.x, p.y)

            # Print location description depending on if player has visited before
            # Add points if player first time visiting
            location.visit(p)

            # If location is MissionLocation, then check if player has items to pick up
            if isinstance(location, MissionLocation):
                location.check_delivery(w, p, location)

            available_actions = location.available_actions

            print("What to do?\n")
            choice = input("\nEnter action: ").lower().strip()

            if choice == 'quit':
                quit_game = True
            else:
                do_action(w, p, location, choice, menu)

            if check_for_victory(p):
                p.victory = True

    if p.victory:
        print('\x1B[3mSome time later...\x1B[0m')
        print('You made it to your exam in time with all your items.')
        print('You feel pretty confident about how you did! The studying paid off, hopefully.')
        print(f'Score: {p.score}')
    elif not quit_game:
        print('You took too long to get to your exam. You missed it.')
        print(f'Score: {p.score}')
    else:
        print('Quitting game...')
