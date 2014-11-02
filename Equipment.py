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
        - right_hand_finger_1: Jewelry
        - right_hand_finger_2: Jewelry
        - left_hand_finger_1: Jewelry
        - left_hand_finger_2: Jewelry
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
        self.right_hand_finger_1 = None
        self.right_hand_finger_2 = None
        self.left_hand_finger_1 = None
        self.left_hand_finger_2 = None
        self.neck = None
        self.wrist = None

    def addWeapon(self, item, hand="right"):
        """
        Add a Weapon in equipement
        - output: None
        """
        try:
            if item.wType in ['twohands', 'bow']:
                self.right_hand = item
                self.left_hand = item
                # Ne pas oublier les effet de l'enchantement
            elif item.wType in ['onehand', 'dagger', 'stick']:
                if hand == 'right':
                    self.right_hand = item
                elif hand == 'left':
                    self.left_hand = item
                else:
                    print("{} n'est pas une position d'arme valide"
                          .format(hand))
            else:
                print("Le type d'arme est invalide")
        except AttributeError:
            print("Cet objet n'est pas une arme")

    def removeWeapon(self, hand="all"):
        """
        Remove a weapon from a hand
        - output: None
        """
        if hand == "right":
            self.right_hand = None
        elif hand == "left":
            self.left_hand = None
        elif hand == "all":
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
            self.head = item
        elif location == "shoulers":
            self.shoulders == item
        elif location == "arms":
            self.arms = item
        elif location == "trunk":
            self.trunk = item
        elif location == "legs":
            self.legs = item
        elif location == "feet":
            self.feet = item
        elif location == "all":
            self.head = None
            self.shoulders = None
            self.arms = None
            self.trunk = None
            self.legs = None
            self.feet = None
        else:
            print("L'emplacement est invalide")

    def addJewelry(self, item, finger=None):
        """
        Add Jewelry in Equipment
        - output: None
        """
        try:
            if item.jType == 'ring':
                if finger == 'right1':
                    self.right_hand_finger_1 = item
                elif finger == 'right2':
                    self.right_hand_finger_2 = item
                elif finger == 'left1':
                    self.left_hand_finger_1 = item
                elif finger == 'left2':
                    self.left_hand_finger_2 = item
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
            self.right_hand_finger_1 = None
        elif location == "right2":
            self.right_hand_finger_2 = None
        elif location == "left1":
            self.left_hand_finger_1 = None
        elif location == "left2":
            self.left_hand_finger_2 = None
        elif location == "neck":
            self.neck = None
        elif location == "wrist":
            self.wrist = None
        elif location == "all":
            self.right_hand_finger_1 = None
            self.right_hand_finger_2 = None
            self.left_hand_finger_1 = None
            self.left_hand_finger_2 = None
            self.neck = None
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

    def addItem(self, item):
        """
        Add an Item in BagPack
        - output: None
        """
        if isinstance(item, Weapon):
            if item in self.weapons:
                self.weapons[item] += 1
            else:
                self.weapons[item] = 1
        elif isinstance(item, Armor):
            if item in self.armors:
                self.armors[item] += 1
            else:
                self.armors[item] = 1
        elif isinstance(item, Jewelry):
            if item in self.jewelries:
                self.jewelries[item] += 1
            else:
                self.jewelries[item] = 1
        elif isinstance(item, Potion):
            if item in self.potions:
                self.potions[item] += 1
            else:
                self.potions[item] = 1
        else:
            if item in self.useless_Items:
                self.useless_Items[item] += 1
            else:
                self.useless_Items[item] = 1

    def removeItem(self, item):
        """
        Remove an Item from BagPack
        - output: None
        """
        if item in self.weapons:
            if self.weapons[item] > 1:
                self.weapons[item] -= 1
            else:
                del self.weapons[item]
        elif item in self.armors:
            if self.armors[item] > 1:
                self.armors[item] -= 1
            else:
                del self.armors[item]
        elif item in self.jewelries:
            if self.jewelries[item] > 1:
                self.jewelries[item] -= 1
            else:
                del self.jewelries[item]
        elif item in self.potions:
            if self.potions[item] > 1:
                self.potions[item] -= 1
            else:
                del self.potions[item]
        elif item in self.useless_Items:
            if self.useless_Items[item] > 1:
                self.useless_Items[item] -= 1
            else:
                del self.useless_Items[item]
        else:
            print("Cet objet n'est pas dans l'inventaire")
