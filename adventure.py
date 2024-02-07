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
from typing import Optional

# Note: You may add helper functions, classes, etc. here as needed


def do_action(world: World, player: Player, player_location: Location, player_choice: str,
              available_actions: Optional[dict[str, str]] = None,
              menu: Optional[list[str]] = None) -> Optional[int]:
    """Handles an action that a player executes in a given world based on player input.
    If action is not a move function, then it prompts player for another action, and recursively calls this function.
    Returns 1 if player quits"""

    player_input = player_choice.lower().split()
    action_input = player_input[0]
    arg = ' '.join(player_input[1:])

    if action_input == 'go':
        if arg == 'north':
            world.move_player(player.x, player.y - 1, player)
            return
        elif arg == 'south':
            world.move_player(player.x, player.y + 1, player)
            return
        elif arg == 'east':
            world.move_player(player.x + 1, player.y, player)
            return
        elif arg == 'west':
            world.move_player(player.x - 1, player.y, player)
            return
        else:
            print('\nInvalid direction. Please go north, east, south, or west.')
    elif action_input == 'pick':
        world.pick(player, player_location, arg)
    elif action_input == 'drop':
        world.drop(player, player_location, arg)
    elif action_input == 'look':
        location.get_long()
    elif action_input == 'quit':
        return 1
    elif action_input == 'inventory':
        inv = []
        for item in p.inventory:
            inv.append(item.name)
        print(', '.join(inv))
    elif action_input == 'open':
        if 'open' not in available_actions:
            print('Nothing can be opened in this location.')
        elif arg in available_actions['open']:
            w.open(location, arg)
        else:
            print(f'You cannot open a {arg}.')

    elif action_input == 'menu':
        print("Menu Options: \n")
        for option in menu:
            print(option)
        print(f'\nActions available at LOCATION {player_location.num}: \n')
        for action in available_actions:
            print(f'{action} [argument]')
            # Print all Item or Furniture objects that an action can be performed on.
            print('\t' + ', '.join(player_location.available_actions[action]) + '\n')
    elif any(action_input == action for action in available_actions):
        obj = None
        # Check if item is in inventory
        if arg in {item.name for item in player.inventory}:
            for item in player.inventory:
                if item.name == arg:
                    obj = item
                    break
        # Check if interactable is in location
        else:
            for interactable in location.interactables:
                if interactable.name == arg:
                    obj = interactable
                    break
        if obj:
            if isinstance(obj, Item):
                obj.do_action(player, action_input)
            else:
                obj.do_action(world, player, player_location, action_input)
        else:
            print(f'{arg} does not exist in your inventory or at this location.')
    else:
        print('Invalid action.')

    # Prompt player for action again
    player_choice = input("\nChoose action: ")
    call = do_action(world, player, player_location, player_choice, available_actions, menu)
    # Check if player called quit
    if call == 1:
        return 1


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


if __name__ == "__main__":
    quit_game = False

    w = World(open("map.txt"), open("locations.txt"), open("items.txt"))
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
        location.visit()
        available_actions = location.available_actions

        print("What to do?\n")
        choice = input("\nEnter action: ").lower().strip()

        call_do_action = do_action(w, p, location, choice, available_actions, menu)

        if call_do_action == 1:
            quit_game = True
            break

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
