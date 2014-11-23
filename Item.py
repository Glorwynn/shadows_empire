from Character import *
from Effect import *


class Item:

    """
        Class for generic Items.
        ========================
        Attributes:
        -----------
            - name: String
            - weight: Integer
            - price: Integer (gold)
    """

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def sell(self, buyer, seller, number=1):
        """
            Sell a number of item from buyer to seller.
            -------------------------------------------
            Add the item from seller to buyer and add the gold
            from buyer to seller.

            OUTPUT: None
        """
        if seller.bagpack.inBagpack(self, number):
            if buyer.gold >= self.price:
                buyer.gold -= self.price
                seller.gold += self.price
                buyer.bagpack.addItem(self)
                seller.bagpack.removeItem(self)
            else:
                print("{} n'a pas l'argent pour acheter {}"
                      .format(buyer.name, self.name))
        else:
            print("{} n'a pas cet objet".format(buyer.name))


class EquipmentItem(Item):

    """
        Class for Items wore by a character.
        ====================================
        Attributes:
            - name: String
            - weight: Integer
            - price: Integer (gold)
            - enchantments: List of effects
            - required level: Integer
    """

    def __init__(self, name, weight, price,
                 enchantments, required_Level):
        Item.__init__(self, name, weight, price)
        self.enchantments = enchantments
        self.required_Level = required_Level

    def equipEffect(self, character):
        """
            Apply item enchantments on the character.
            -----------------------------------------
            For each effect, the corresponding attribute is upgraded.

            OUTPUT: None
        """
        for effect in self.enchantments:
            effect.apply(character)

    def unequipEffect(self, character):
        """
            Disapply enchantments on the character.
            ---------------------------------------
            For each effect, the corresponding attribute is downgraded.
            OUTPUT: None
        """
        for effect in self.enchantments:
            effect.disapply(character)


class Weapon(EquipmentItem):

    """
        Class for weapons.
        ==================
        Attributes:
        -----------
            - name: String
            - weight: Integer
            - price: Integer (gold)
            - enchantments: List of effects
            - required level: Integer (???)
            - damages: ???
            - wType: str[onehand, twohands, bow, dagger, stick]
    """

    def __init__(self, name, weight, price,
                 enchantments, required_Level, damages, wType):
        EquipmentItem.__init__(self, name, weight,
                               price, enchantments, required_Level)
        self.damages = damages
        self.wType = wType


class Armor(EquipmentItem):

    """
        Class for armor pieces.
        =======================
        Attributes:
        -----------
            - name: String
            - weight: Integer
            - price: Integer (gold)
            - enchantments: List of Effects
            - required level: Integer (???)
            - resistance: Integer
            - location: str[head, shoulders, arms, hands, trunk, legs, feet]
    """

    def __init__(self, name, weight, price,
                 enchantments, required_Level, resistance, location):
        EquipmentItem.__init__(self, name, weight,
                               price, enchantments, required_Level)
        self.resistance = resistance
        self.location = location


class Jewelry(EquipmentItem):

    """
        Class for Jewelries.
        ====================
        Attributes:
        -----------
            - name: String
            - weight: Integer
            - price: Integer (gold)
            - enchantments: List of Effects
            - required level: Integer (???)
            - jType: str[ring, necklace, armlet]
    """

    def __init__(self, name, weight, price,
                 enchantments, required_Level, jType):
        EquipmentItem.__init__(self, name, weight, price,
                               enchantments, required_Level)
        self.jType = jType


class Potion(Item):

    """
        Class for Potions.
        ==================
        Attributes:
        -----------
            - name: String
            - weight: Integer
            - price: Integer (gold)
            - effects: List of Effects
            - delay: Integer
    """

    def __init__(self, name, weight, price,
                 effects, delay):
        Item.__init__(self, name, weight, price)
        self.effects = effects
        self.delay = delay

    def actEffect(self, character):
        """
            Apply effects of item on character while delay.
            -----------------------------------------------
            For each effects, the corresponding arrtibute is upgraded
            OUTPUT: None
        """
        for effect in self.effects:
            effect.act(character)
