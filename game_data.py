"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from __future__ import annotations
from typing import Optional, TextIO, Union, Any


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - num:
            The unique location number for this location.
        - points:
            The number of points a player receives for visiting this location.
        - brief:
            A brief description of this location.
        - long:
            A long description of this location.
        - available_actions:
            A list of all available actions/commands.
        - interactables:
            A list of Item and Furniture objects that can be found and interacted with in this location.
            If empty, the location has nothing to examine.
        - visited:
            Boolean that is True if player has been to this location already.
            Otherwise, visited is False.

    Representation Invariants:
        - num >= -1
        - brief != ''
        - long != ''
    """
    num: int
    points: int
    brief: str
    long: str
    available_actions: dict
    interactables: list[Union[Item, Furniture]]
    visited: bool

    def __init__(self, num, points, brief, long) -> None:
        """Initialize a new location.
        """

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.

        self.num = num
        self.points = points
        self.brief = brief
        self.long = long
        self.available_actions = {}
        self.interactables = []
        self.visited = False

    def available_actions(self) -> str:
        """
        Return the available actions in this location.
        The actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        """
        return "\n".join(self.available_actions)

    def get_coordinates(self, world: World) -> Optional[tuple[int, int]]:
        """Return coordinates of this location in a given world.
        If this location number is -1, then self.get_coordinates returns None.

        Preconditions:
            - self.num in {n for row in map for n in row}
        """
        if self.num == -1:
            return
        for y in range(0, len(world.map)):
            for x in range(0, len(world.map[0])):
                if world.map[y][x] == self.num:
                    return x, y


class MissionLocation(Location):
    """A location that completes a "mission" when a player enters this location with a specified Item object
    in their inventory.

    Instance Attributes:
        - item_to_deliver:
            The name of the Item object that a player must have in their inventory
            when visiting this location.
        - item_to_receive:
            The name of the Item object that a player receives
            when item to deliver is delivered.

    Representation invariants:
        - item_to_deliver != ''
        - item_to_receive != ''
    """

    def __init__(self, num, points, brief, long, item_to_deliver, item_to_receive):
        super().__init__(num, points, brief, long)
        self.item_to_deliver = item_to_deliver
        self.item_to_receive = item_to_receive


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name:
            The name of this item.
        - points:
            The amount of points a player receives for picking up this item.
        - actions:
            A dictionary of available actions for this item. The keys are the action calls.
            The values are text output that should be returned for calling those actions.
        - stored_in_furniture:
            Name of the Furniture that this Item is stored in.
            If it is not stored in a Location, then this is an empty string.
        - picked_up:
            Indicates whether this item has ever been picked up by a player.
            True if it has ever been picked up. Otherwise, picked_up is False.
        - cur_picked_up:
            Indicates whether this item is currently picked up by a player.
            True if currently picked up by player. Otherwise, False.

    Representation Invariants:
        - name != ""
    """

    def __init__(self, name: str, points: int, actions: dict[str, str], stored_in_furniture: Optional[str] = None):
        self.name = name
        self.points = points
        self.actions = {'pick': f'You have picked up {self.name}.', 'drop': f'You have dropped {self.name}.'}
        if stored_in_furniture:
            self.stored_in_furniture = stored_in_furniture
        else:
            self.stored_in_furniture = ''
        self.picked_up = False
        self.cur_picked_up = False
        for action in actions:
            self.add_action(action, actions[action])

    def add_action(self, action: str, argument: str):
        """Add or mutate an action in self.actions.
        If the action is pick or drop, then the action argument must
        be appended to the actions.
        """
        if action == 'pick' or action == 'drop':
            self.actions[action] += f'\n{argument}'
        else:
            self.actions[action] = argument

    def remove_action(self, action: str):
        """Remove an action for this item."""
        if action in self.actions:
            self.actions.pop(action)

    def execute_action(self, action: str, player: Player) -> str:
        """Execute an action for this item."""
        if action in self.actions:
            # Execute the action here
            pass
        # Could use try except statement here
        # If player not in

    def get_actions(self):
        """Return all actions keys in self.actions."""
        pass

    def picked_up(self, player):
        """Returns whether this item has ever been picked up by a player."""
        return self.picked_up


class MissionItem(Item):
    """A special item that can be received when a player has completed a mission.
    These items cannot be picked up by players unless if the mission has been completed.

    Instance Attributes:
        - mission_completed:
            Indicates whether the mission has been completed.

    Representation Invariants:
        - name != ''
        - points > 0
    """
    mission_completed: bool

    def __init__(self, name: str, points: int, actions: dict[str, str]) -> None:
        super().__init__(name, points, actions)
        self.mission_completed = False

    def mission_completed(self):
        """Updates this mission_completed attribute to be True"""
        self.mission_completed = True

    # TODO: Make pick/drop unique methods!!!


class PowerUp(Item):
    """A power up item in our text adventure game world.

    Instance Attributes:
        - moves_back:
            The number of moves that a player gets deducted from their total.
            Moves are only deducted the first time a player picks up this item
        - picked_up:
            Boolean value that is True when a player has already picked up this item

    Representation Invariants:
        - # TODO
    """

    def __init__(self, name, points, actions, moves_back):
        super().__init__(name, points, actions, False)
        self.moves_back = moves_back


class Furniture:
    """An interactable furniture in our text adventure game world.

    Instance Attributes:
        - name:
            The name of this furniture
        - points:
            Points that a player earns for examining this furniture
        - items:
            A list of items that can be found inside of this furniture
        - actions:
            A mapping representation of actions to their text output when
            action is performed

    Representation Invariants:
        - name != ''
        - points >= 0
    """
    name: str
    points: int
    items: list[Item]
    actions: dict[str, str]

    def __init__(self, name: str, points: int, actions: dict[str, str]) -> None:
        """Initialize a new Furniture.
        """
        self.name = name
        self.points = points
        self.items = []
        self.actions = actions

    def add_actions(self, action: str, output: str) -> None:
        """Add an action to this Furniture."""
        self.actions[action] = output


class LockedFurniture(Furniture):
    """An interactable locked furniture in our text adventure game world.

    Instance Attributes:
        - name:
            The name of this locked furniture
        - points:
            Points that a player earns for examining this locked furniture
        - key:
            Password required for a player to "open" this locked furniture
        - items:
            A list of items that can be found inside of this locked furniture.
            If there are no items in this Furniture, the list is empty.

    Representation Invariants:
        - name != ''
        - points >= 0
    """

    def __init__(self, name: str, points: int, key: str, items: Optional[list[Item]] = None) -> None:
        """Initialize a new LockedFurniture.
        """
        super().__init__(name, points)
        self.items = []
        self.add_actions('open', f'You have opened {self.name}')
        self.key = key
        # If items is not None, add it to self.items
        if items:
            for item in items:
                self.items.append(item)


class Player:
    """
    A Player in the text adventure game.

    Instance Attributes:
        - x:
            The player's x coordinate on the map.
        - y:
            The player's y coordinate on the map.
        - inventory:
            Objects that the player has picked up.
        - victory:
            The player's victory status
        - world:


    Representation Invariants:
        - # TODO
    """

    def __init__(self, x: int, y: int, world: World) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.world = world
        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False

    def move(self, direction: str) -> None:
        """
        Moves the player one unit in the direction selected by the player. Possible directions are
        (north, east, south, west).
        """
        if direction.lower() == 'north':
            if self.world.map[self.y - 1][self.x] == -1:
                pass
            else:
                self.y -= 1
        elif direction.lower() == 'east':
            if self.world.map[self.y][self.x + 1] == -1:
                pass
            else:
                self.x += 1
        elif direction.lower() == 'south':
            if self.world.map[self.y + 1][self.x] == -1:
                pass
            else:
                self.y = 1
        elif direction.lower() == 'west':
            if self.world.map[self.y][self.x - 1] == -1:
                pass
            else:
                self.x -= 1
        else:
            print("This is not a valid direction. Try entering a valid one!")


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map:
            A nested list representation of this world's map
        - locations:
            A list representation of all Location objects of this world's map
        - interactables:
            A mapping representation of Location numbers to Item and Furniture objects found in
            the locations of this world's map

    Representation Invariants:
        - # TODO
    """
    map: list[list[int]]
    locations: list[Location]
    interactables: dict[int, list[Union[Furniture, Item]]]

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)
        self.locations = self.load_locations(location_data)
        self.interactables = self.load_items(items_data)

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """
        world_map = []

        for line in map_data:
            filtered_row = [int(char) for char in line.split()]
            world_map.append(filtered_row)

        return world_map

    def load_locations(self, location_data: TextIO) -> list[Location]:
        """Store locations from open file location_data as the locations attribute of this object.
        Locations are stored in a list.
        """
        self.locations = []

        line = location_data.readline()

        # Cycle through the lines in location.txt that indicate a template
        while line != '\n':
            line = location_data.readline()

        # Read locations until EOF
        while line:
            is_mission_location = False
            item_to_deliver = ''
            item_to_receive = ''

            # Read location number
            line = location_data.readline()
            try:
                location_number = int(line)
            except ValueError:  # Special mission location
                is_mission_location = True
                substrings = line.split(',')
                location_number = int(substrings[0])
                item_to_deliver = substrings[1].split(':::')[1]
                item_to_receive = substrings[2].strip()

            # Read location points
            line = location_data.readline()
            points = int(line)

            # Read brief description
            line = location_data.readline()
            brief = line.strip()

            # Read long description
            line = location_data.readline()
            long = ''
            while line.strip() != 'END':
                long += line
                line = location_data.readline()

            line = location_data.readline()
            assert line.strip() == ''

            if not is_mission_location:
                self.locations.append(Location(
                    location_number, points, brief, long)
                )
            else:
                self.locations.append(MissionLocation(
                    location_number, points, brief, long, item_to_deliver, item_to_receive)
                )

        return self.locations

    def load_items(self, items_data: TextIO) -> dict[int, list[Union[Item, Furniture]]]:
        """Store items from open file items_data as the items attribute of this object.
        Items are stored in a mapping that maps a location number to its corresponding Items in a list like so:

        If item1 and item2 are Item objects found in location 0, then load_items should assign this
        World object's items to be {-1: [], 0: [item1, item2]}.
        """
        interactables_so_far = {}

        line = items_data.readline()

        # Cycle through the lines in items.txt that indicate a template
        while line != '\n':
            line = items_data.readline()

        # Read lines until EOF
        line = items_data.readline()

        while line:
            # Determine whether Item is found in a location or inside Furniture object
            # a location
            stored_in_furniture = ''
            try:
                stored_in_location = int(line)
            except ValueError:  # Item is stored in a furniture object
                stored_in_location = int(line.split(':::')[0])
                stored_in_furniture = line.split(':::')[1].strip()

            # Read interactable type
            line = items_data.readline()
            object_type = line.strip()

            line = items_data.readline()

            # Check object type as format changes if LF (LockedFurniture)
            # or MF (MissionFurniture) or PU (PowerUp)
            pu_moves_back = 0

            if object_type == 'LF':
                # Read key value
                key = line.strip()
                line = items_data.readline()
            elif object_type == 'MF':
                # Read item given, to deliver, and to receive respectively
                args = line.split(',')
                assert len(args) == 3
                item_given = args[0]
                item_to_deliver = args[1]
                item_to_receive = args[2].strip()
                line = items_data.readline()
            elif object_type == 'PU':
                pu_moves_back = int(line)
                line = items_data.readline()

            # Read interactable name
            name = line.strip()

            # Read points
            line = items_data.readline()
            points = int(line)

            # Read actions
            actions = {}
            line = items_data.readline()
            while line.strip() != 'END':
                args = line.split(':::')
                actions[args[0]] = args[1].strip()
                line = items_data.readline()

            # Create new interactable objects based on type
            for loc in self.locations:
                if loc.num == stored_in_location:
                    if object_type == 'F':
                        # Create new Furniture object
                        new_furniture = Furniture(name, points, actions)
                        # Add Furniture to interactables_so_far
                        if stored_in_location in interactables_so_far:
                            interactables_so_far[stored_in_location] += [new_furniture]
                        else:
                            interactables_so_far[stored_in_location] = [new_furniture]
                    elif object_type == 'I' or object_type == 'M':
                        new_item = Item(name, points, actions, stored_in_furniture)
                        # Add Item to interactables_so_far
                        if stored_in_location in interactables_so_far:
                            interactables_so_far[stored_in_location] += [new_item]
                        else:
                            interactables_so_far[stored_in_location] = [new_item]
                        if stored_in_furniture:
                            # Find Furniture it is stored in
                            for furniture in interactables_so_far[stored_in_location]:
                                if furniture.name == stored_in_furniture:
                                    # Add item to Furniture
                                    furniture.items.append(new_item)
                                    break
                    elif object_type == 'PU':
                        new_powerup = PowerUp(name, points, actions, pu_moves_back)
                        # Add PowerUp to interactables_so_far
                        if stored_in_location in interactables_so_far:
                            interactables_so_far[stored_in_location] += [new_powerup]
                        else:
                            interactables_so_far[stored_in_location] = [new_powerup]
                    elif object_type == 'M':
                        new_mission_item = MissionItem(name, points, actions)
                        # Add MissionItem to interactables_so_far
                        if stored_in_location in interactables_so_far:
                            interactables_so_far[stored_in_location] += [new_mission_item]
                        else:
                            interactables_so_far[stored_in_location] = [new_mission_item]

                    break

            items_data.readline()
            line = items_data.readline()

        return interactables_so_far

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """
        try:
            location_number = self.map[y][x]

            # Check if location_number is -1
            if location_number == -1:
                return None

            for location in self.locations:
                if location.num == location_number:
                    return location

        except IndexError:
            return None


# --------- Exceptions ---------
class DirectionError(Exception):
    """Exception raised when direction is invalid."""
    def __str__(self) -> str:
        """Return a string representation of this error."""
        return 'Invalid direction'
