from Character import *
from Effect import *


class Item:

    """
    Class for generic Items.
    Parameters:
        - name: String
        - weight: Integer
        - value: Integer (gold)
    """

    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value


class EquipmentItem(Item):

    """
    Class for Items wore by a character.
    Parameters:
        - name: String
        - weight: Integer
        - value: Integer (gold)
        - enchantments: List of Effects
        - required level: Integer (???)
    """

    def __init__(self, name, weight, value,
                 enchantments, required_Level):
        Item.__init__(self, name, weight, value)
        self.enchantments = enchantments
        self.required_Level = required_Level

    def equipEffect(character):
        """
        Apply enchantments on the character
        - output: None
        """
        for effect in enchantments:
            effect.apply(character)

    def unequipEffect(character):
        """
        Disapply enchantments on the character
        - output: None
        """
        for effect in enchantments:
            effect.disapply(character)


class Weapon(EquipmentItem):

    """
    Class for weapons.
    Parameters:
        - name: String
        - weight: Integer
        - value: Integer (gold)
        - enchantments: List of Effects
        - required level: Integer (???)
        - damages: ???
        - wType: str[onehand, twohands, bow, dagger, stick]
    """

    def __init__(self, name, weight, value,
                 enchantments, required_Level, damages, wType):
        EquipmentItem.__init__(self, name, weight,
                               value, enchantments, required_Level)
        self.damages = damages
        self.wType = wType


class Armor(EquipmentItem):

    """
    Class for armor pieces.
    Parameters:
        - name: String
        - weight: Integer
        - value: Integer (gold)
        - enchantments: List of Effects
        - required level: Integer (???)
        - resistance: Integer
        - location: str[head, shoulders, arms, hands, trunk, legs, feet]
    """

    def __init__(self, name, weight, value,
                 enchantments, required_Level, resistance, location):
        EquipmentItem.__init__(self, name, weight,
                               value, enchantments, required_Level)
        self.resistance = resistance
        self.location = location


class Jewelry(EquipmentItem):

    """
    Class for Jewelries.
    Parameters:
        - name: String
        - weight: Integer
        - value: Integer (gold)
        - enchantments: List of Effects
        - required level: Integer (???)
        - jType: str[ring, necklace, armlet]
    """

    def __init__(self, name, weight, value,
                 enchantments, required_Level, jType):
        EquipmentItem.__init__(self, name, weight, value,
                      enchantments, required_Level)
        self.jType = jType


class Potion(Item):

    """
    Class for generic Items.
    Parameters:
        - name: String
        - weight: Integer
        - value: Integer (gold)
        - effects: List of Effects
    """

    def __init__(self, name, weight, value,
                 effects):
        Item.__init__(self, name, weight, value)
        self.effects = effects

    def actEffect(self, character):
        """
        Apply effects of object on character.
        - output: None
        """
        for effect in self.effects:
            effect.act(character)
