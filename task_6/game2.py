"""
In this file, we'll create the main game loop and control the
flow of the game.
"""
class Street():
    """
    This class represents a street in the game.
    """
    def __init__(self, street_name: str):
        self.street_name = street_name
        self.linked_streets = {}
        self.street_description = None
        self.street_to_link = None
        self.direction = None
        self.character = None
        self.item = None

    def set_description(self, street_description: str):
        """
        This method sets the description of the street.
        """
        self.street_description = street_description

    def get_description(self) -> str:
        """
        This method returns the description of the street.
        """
        return self.street_description

    def link_street(self, street_to_link: str, direction: str):
        """
        This method links this street to another street in the given direction.
        """
        self.linked_streets[direction] = street_to_link

    def set_character(self, character: str):
        """
        This method sets the character in the street.
        """
        self.character = character

    def get_character(self) -> str:
        """
        This method returns the character in the street.
        """
        return self.character

    def set_item(self, item: str):
        """
        This method sets the item in the street.
        """
        self.item = item

    def get_item(self) -> str:
        """
        This method returns the item in the street.
        """
        return self.item

    def get_details(self) -> str:
        """
        This method prints the details of the street.
        """
        print(self.street_name)
        print('--------------------')
        print(self.street_description)
        for direction, name in self.linked_streets.items():
            print(f'Вулиця {name.street_name} розташована {direction}')

    def move(self, direction: str) -> str:
        """
        This method moves the player to the street in the given direction.
        """
        if direction in self.linked_streets:
            return self.linked_streets[direction]
        return None


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
        print(f'Можна підібрати [{self.item_name}] - {self.item_description}')

    def get_name(self) -> str:
        """
        This method returns the name of the item.
        """
        return self.item_name


class Character:
    """
    This class represents an character in the game.
    """
    def __init__(self, habit_name, description):
        self.habit_name = habit_name
        self.description = description
        self.conversation = None

    def set_conversation(self, conversation: str):
        """
        This method sets the conversation of the character.
        """
        self.conversation = conversation

    def describe(self) -> str:
        """
        This method prints the description of the character.
        """
        print(f'{self.habit_name} тут!')
        print(self.description)

    def talk(self) -> str:
        """
        This method prints the conversation of the character.
        """
        print(f'[{self.habit_name} каже]: {self.conversation}')


class Enemy(Character):
    """
    This class represents an enemy in the game.
    """
    def __init__(self, habit_name, description):
        super().__init__(habit_name, description)
        self.weakness = None

    def set_conversation(self, conversation: str):
        """
        This method sets the conversation of the enemy.
        """
        super().set_conversation(conversation)

    def set_weakness(self, weakness: str):
        """
        This method sets the weakness of the enemy.
        """
        self.weakness = weakness

    def describe(self) -> str:
        """
        This method prints the description of the enemy.
        """
        super().describe()

    def talk(self) -> str:
        """
        This method prints the conversation of the enemy.
        """
        super().talk()

    def fight(self, combat_item: str) -> str:
        """
        This method allows the player to fight the enemy.
        """
        if combat_item == self.weakness:
            print(f'Ти поборов {self.habit_name} завдяки {combat_item}')
            return True
        else:
            print(f'{self.habit_name} розніс тебе')
            return False


class Friend(Character):
    """
    This class represents an character in the game.
    """
    def __init__(self, habit_name, description):
        super().__init__(habit_name, description)

    def set_conversation(self, conversation: str):
        """
        This method sets the conversation of the character.
        """
        super().set_conversation(conversation)

    def describe(self) -> str:
        """
        This method prints the description of the character.
        """
        super().describe()

    def talk(self) -> str:
        """
        This method prints the conversation of the character.
        """
        super().talk()

    def help(self):
        print("Я моку можу тобі допомогти")
