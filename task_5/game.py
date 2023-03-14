"""
In this file, we'll create the main game loop and control the
flow of the game.
"""
class Room():
    """
    This class represents a room in the game.
    """
    def __init__(self, room_name: str):
        self.room_name = room_name
        self.linked_rooms = {}
        self.room_description = None
        self.room_to_link = None
        self.direction = None
        self.character = None
        self.item = None

    def set_description(self, room_description: str):
        """
        This method sets the description of the room.
        """
        self.room_description = room_description

    def get_description(self) -> str:
        """
        This method returns the description of the room.
        """
        return self.room_description

    def link_room(self, room_to_link: str, direction: str):
        """
        This method links this room to another room in the given direction.
        """
        self.linked_rooms[direction] = room_to_link

    def set_character(self, character: str):
        """
        This method sets the character in the room.
        """
        self.character = character

    def get_character(self) -> str:
        """
        This method returns the character in the room.
        """
        return self.character

    def set_item(self, item: str):
        """
        This method sets the item in the room.
        """
        self.item = item

    def get_item(self) -> str:
        """
        This method returns the item in the room.
        """
        return self.item

    def get_details(self) -> str:
        """
        This method prints the details of the room.
        """
        print(self.room_name)
        print('--------------------')
        print(self.room_description)
        for direction, name in self.linked_rooms.items():
            print(f'The {name.room_name} is {direction}')

    def move(self, direction: str) -> str:
        """
        This method moves the player to the room in the given direction.
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        return None


class Enemy:
    """
    This class represents an enemy in the game.
    """

    defeated = 0

    def __init__(self, habit_name, description):
        self.habit_name = habit_name
        self.description = description
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation: str):
        """
        This method sets the conversation of the enemy.
        """
        self.conversation = conversation

    def set_weakness(self, weakness: str):
        """
        This method sets the weakness of the enemy.
        """
        self.weakness = weakness

    def describe(self) -> str:
        """
        This method prints the description of the enemy.
        """
        print(f'{self.habit_name} is here!')
        print(self.description)

    def talk(self) -> str:
        """
        This method prints the conversation of the enemy.
        """
        print(f'[{self.habit_name} says]: {self.conversation}')

    def fight(self, combat_item: str) -> str:
        """
        This method allows the player to fight the enemy.
        """
        if combat_item == self.weakness:
            print(f'You fend {self.habit_name} off with the {combat_item}')
            Enemy.defeated += 1
            return True
        else:
            print(f'{self.habit_name} crushes you, puny adventurer')
            return False

    def get_defeated(self) -> int:
        """
        This method returns the number of enemies defeated.
        """
        return Enemy.defeated


class Item:
    """
    This class represents an item in the game.
    """
    def __init__(self, item_name):
        self.item_name = item_name
        self.item_description = None

    def set_description(self, item_description: str):
        """
        This method sets the description of the item.
        """
        self.item_description = item_description

    def describe(self) -> str:
        """
        This method prints the description of the item.
        """
        print(f'The [{self.item_name}] is here - {self.item_description}')

    def get_name(self) -> str:
        """
        This method returns the name of the item.
        """
        return self.item_name
