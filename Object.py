from Character import *
from Effect import *


class Item:

    """
    Class for generic Items.
    Parameters:
        - idItem: Integer
        - name: String
        - weight: Integer
        - value: Integer (gold)
    """

    def __init__(self, idItem, name, weight, value):
        self.idItem = idItem
        self.name = name
        self.weight = weight
        self.value = value


class EquipmentItem(Item):

    """
    Class for Items wore by a character.
    Parameters:
        - idItem: Integer
        - name: String
        - weight: Integer
        - value: Integer (gold)
        - enchantments: List of Effects
        - required level: Integer (???)
    """

    def __init__(self, idItem, name, weight, value,
                 enchantments, required_Level):
        Item.__init__(self, idItem, name, weight, value)
        self.enchantments = enchantments
        self.required_Level


class Weapon(EquipmentItem):

    """
    Class for weapons.
    Parameters:
        - idItem: Integer
        - name: String
        - weight: Integer
        - value: Integer (gold)
        - enchantments: List of Effects
        - required level: Integer (???)
        - damages: ???
        - wType: str[onehand, twohands, bow, dagger, stick]
    """

    def __init__(self, idItem, name, weight, value,
                 enchantments, required_Level, damages, wType):
        EquipmentItem.__init__(self, idItem, name, weight,
                               value, enchantments, required_Level)
        self.damages = damages
        self.wType = wType


class Armor(EquipmentItem):

    """
    Class for armor pieces.
    Parameters:
        - idItem: Integer
        - name: String
        - weight: Integer
        - value: Integer (gold)
        - enchantments: List of Effects
        - required level: Integer (???)
        - resistance: Integer
        - location: str[head, shoulders, arms, hands, trunk, legs, feet]
    """

    def __init__(self, idItem, name, weight, value,
                 enchantments, required_Level, resistance, location):
        Item.__init__(self, idItem, name, weight, value,
                      enchantments, required_Level)
        self.resistance = resistance
        self.aType = aType


class Jewelry(EquipmentItem):

    """
    Class for Jewelries.
    Parameters:
        - idItem: Integer
        - name: String
        - weight: Integer
        - value: Integer (gold)
        - enchantments: List of Effects
        - required level: Integer (???)
        - jType: str[ring, necklace, armlet]
    """

    def __init__(self, idItem, name, weight, value,
                 enchantments, required_Level, jType):
        Item.__init__(self, idItem, name, weight, value,
                      enchantments, required_Level)
        self.jType = jType


class Potion(Item):

    """
    Class for generic Items.
    Parameters:
        - idItem: Integer
        - name: String
        - weight: Integer
        - value: Integer (gold)
        - effects: List of Effects
    """

    def __init__(self, idItem, name, weight, value,
                 effects):
        Item.__init__(self, idItem, name, weight, value)
        self.effects = effects

    def actEffect(self, character):
        """
        Apply effects of object on character.
        - output: None
        """
        for effect in self.effects:
            effect.act(character)
