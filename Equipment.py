from Item import *


class Equipment:

    """
    Class for equipement of character
    Paramters:
        - head: Armor
        - shoulders: Armor
        - arms: Armor
        - hands: Armor
        - trunk: Armor
        - legs: Armor
        - feet: Armor
        - right_hand: Weapon
        - left_hand: Weapon
        - right1: Jewelry
        - right2: Jewelry
        - left1: Jewelry
        - left2: Jewelry
        - neck: Jewelry
        - wrist: Jewelry
    """

    def __init__(self):
        self.head = None
        self.shoulders = None
        self.arms = None
        self.hands = None
        self.trunk = None
        self.legs = None
        self.feet = None
        self.right_hand = None
        self.left_hand = None
        self.right1 = None
        self.right2 = None
        self.left1 = None
        self.left2 = None
        self.neck = None
        self.wrist = None

    def addWeapon(self, item, hand="right_hand"):
        """
        Add a Weapon in equipement
        - output: None
        """
        try:
            if item.wType in ['twohands', 'bow']:
                self.right_hand = item
                self.left_hand = item
            elif item.wType in ['onehand', 'dagger', 'stick']:
                if hand == 'right_hand':
                    self.right_hand = item
                elif hand == 'left_hand':
                    self.left_hand = item
                else:
                    print("{} n'est pas une position d'arme valide"
                          .format(hand))
            else:
                print("Le type d'arme est invalide")
        except AttributeError:
            print("Cet objet n'est pas une arme")

    def removeWeapon(self, hand="right_hand"):
        """
        Remove a weapon from a hand
        - output: None
        """
        if(not(self.right_hand is None) and
           self.right_hand.wType in ['twohands', 'bow']):
            self.right_hand = None
            self.left_hand = None
        else:
            if hand == "right_hand":
                if(not(self.right_hand is None) and
                   self.right_hand.wType in ['twohands', 'bow']):
                    self.left_hand = None
                self.right_hand = None
            elif hand == "left_hand":
                if self.left_hand.wType in ['twohands', 'bow']:
                    self.right_hand = None
                self.left_hand = None
            else:
                print("L'emplacement n'est pas valide")

    def addArmor(self, item):
        """
        Add an Armor in equipement
        - output: None
        """
        try:
            if item.location == "head":
                self.head = item
            elif item.location == "shoulers":
                self.shoulders = item
            elif item.location == "arms":
                self.arms = item
            elif item.location == "trunk":
                self.trunk = item
            elif item.location == "legs":
                self.legs = item
            elif item.location == "feet":
                self.feet = item
            else:
                print("L'emplacement d'armure est invalide")
        except AttributeError:
            print("Cet objet n'est pas une armure")

    def removeArmor(self, location="all"):
        if location == "head":
            self.head = None
        elif location == "shoulers":
            self.shoulders == None
        elif location == "arms":
            self.arms = None
        elif location == "trunk":
            self.trunk = None
        elif location == "legs":
            self.legs = None
        elif location == "feet":
            self.feet = None
        else:
            print("L'emplacement est invalide")

    def addJewelry(self, item, finger='right1'):
        """
        Add Jewelry in Equipment
        - output: None
        """
        try:
            if item.jType == 'ring':
                if finger == 'right1':
                    self.right1 = item
                elif finger == 'right2':
                    self.right2 = item
                elif finger == 'left1':
                    self.left1 = item
                elif finger == 'left2':
                    self.left2 = item
                else:
                    if finger is None:
                        print("Il faut indiquer sur quel doigt" +
                              "mettre cet objet")
                    else:
                        print("L'emplacement est invalide")
            elif item.jType == 'necklace':
                self.neck = item
            elif item.jType == 'armlet':
                self.wrist = item
            else:
                print("Le type de bijou est invalide")
        except AttributeError:
            print("Cet objet n'est pas un bijou")

    def removeJewelry(self, location="all"):
        if location == "right1":
            self.right1 = None
        elif location == "right2":
            self.right2 = None
        elif location == "left1":
            self.left1 = None
        elif location == "left2":
            self.left2 = None
        elif location == "neck":
            self.neck = None
        elif location == "wrist":
            self.wrist = None
        else:
            print("Cet emplacement n'est pas valide")


class BagPack:

    """
    Class for BagPack of character
    Parameters:
        - potions: Dictionnary of Potion
        - weapons: Dictionnary of Weapon
        - armors: Dictionnary of Armor
        - jewelries: Dictionnary of Jewelry
        - useless_Items: Dictionnary of other Items
    """

    def __init__(self):
        self.potions = {}
        self.weapons = {}
        self.armors = {}
        self.jewelries = {}
        self.useless_Items = {}

    def addItem(self, item, number):
        """
        Add an Item in BagPack
        - output: None
        """
        if isinstance(item, Weapon):
            if item in self.weapons:
                self.weapons[item] += number
            else:
                self.weapons[item] = number
        elif isinstance(item, Armor):
            if item in self.armors:
                self.armors[item] += number
            else:
                self.armors[item] = number
        elif isinstance(item, Jewelry):
            if item in self.jewelries:
                self.jewelries[item] += number
            else:
                self.jewelries[item] = number
        elif isinstance(item, Potion):
            if item in self.potions:
                self.potions[item] += number
            else:
                self.potions[item] = number
        else:
            if item in self.useless_Items:
                self.useless_Items[item] += number
            else:
                self.useless_Items[item] = number

    def removeItem(self, item, number):
        """
        Remove an Item from BagPack
        - output: None
        """
        if item in self.weapons:
            if self.weapons[item] > number:
                self.weapons[item] -= number
            else:
                del self.weapons[item]
        elif item in self.armors:
            if self.armors[item] > number:
                self.armors[item] -= number
            else:
                del self.armors[item]
        elif item in self.jewelries:
            if self.jewelries[item] > number:
                self.jewelries[item] -= number
            else:
                del self.jewelries[item]
        elif item in self.potions:
            if self.potions[item] > number:
                self.potions[item] -= number
            else:
                del self.potions[item]
        elif item in self.useless_Items:
            if self.useless_Items[item] > number:
                self.useless_Items[item] -= number
            else:
                del self.useless_Items[item]
        else:
            print("Cet objet n'est pas dans l'inventaire")
