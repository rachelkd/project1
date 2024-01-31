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
from typing import Optional, TextIO, Union


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

    def __init__(self) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
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
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.

        # TODO: Complete this method

    def available_actions(self) -> str:
        """
        Return the available actions in this location.
        The actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        """
        return "\n".join(self.available_actions)


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name:
            The name of this item.
        - points:
            The amount of points a player receives for picking up this item.
        - actions:
            A dictionary of available actions for this item. The keys are the action calls.
            The values are text output that should be returned for calling those actions
        - picked_up:
            Indicates whether this item has ever been picked up by a player.
            True if it has ever been picked up. Otherwise, picked_up is False.
        - cur_picked_up:
            Indicates whether this item is currently picked up by a player.
            True if currently picked up by player. Otherwise, False.

    Representation Invariants:
        - name != ""
    """
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.actions = {'pick': f'You have picked up {self.name}.'}
        self.picked_up = False
        self.cur_picked_up = False

    def add_action(self, action: str, argument: str):
        """Add or mutate an action in self.actions."""
        self.actions[action] = argument

    def remove_action(self, action: str):
        """Remove an action in self.actions if needed."""
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
    def __init__(self, name, points, moves_back):
        super().__init__(name, points)
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

    Representation Invariants:
        - name != ''
        - points >= 0
    """

    def __init__(self, name: str, points: int, items: Optional[list[Item]] = None) -> None:
        """Initialize a new item.
        """

        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.points = points
        self.items = items


class LockedFurniture:
    """An interactable locked furniture in our text adventure game world.

    Instance Attributes:
        - name:
            The name of this locked furniture
        - points:
            Points that a player earns for examining this locked furniture
        - items:
            A list of items that can be found inside of this locked furniture
        - key:
            Password required for a player to "open" this locked furniture

    Representation Invariants:
        - name != ''
        - points >= 0
    """

    def __init__(self, name: str, points: int, items: Optional[list[Item]] = None) -> None:
        """Initialize a new item.
        """

        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.points = points
        self.items = items


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - # TODO add more instance attributes as needed; do NOT remove the map attribute

    Representation Invariants:
        - # TODO
    """

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

        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

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

        # TODO: Complete this method as specified. Do not modify any of this function's specifications.

    # TODO: Add methods for loading location data and item data (see note above).

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """

        # TODO: Complete this method as specified. Do not modify any of this function's specifications.
