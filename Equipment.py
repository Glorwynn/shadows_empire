from Object import *


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

    def addArmor(self, item):
        """
        Add an Armor in equipement
        - output: None
        """
        if item.location == "head":
            self.head = item
        elif item.location == "shoulers":
            self.shoulders == item
        elif item.location == "arms":
            self.arms = item
        elif item.location == "trunk":
            self.trunk = item
        elif item.location == "legs":
            self.legs = item
        elif item.location == "feet":
            self.feet = item
        else:
            print("L'emplacement d'arume est invalide")

    def addJewelry(self, item, finger=None):
        """
        Add Jewelry in Equipment
        - output: None
        """
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

    def equip(self, item, ):
        """
        Equip an item
        - output: None
        """
        if type(item) == Weapon:
            self.equipWeapon()
        elif type(item) == Armor:
            self.setParam(item.location, item)
        else:
            print("Vous ne pouvez pas equiper cet objet")

    def unequip(self, location):
        if location is None:
            print('Vous ne portez rien à cet endroit')
        else:
            location = None

    def setParam(string, value):
        if string == 'head':
            self.head = value
        elif string == 'shoulders':
            self.shoulders = value
        elif string == 'arms':
            self.arms = value
        elif string == 'hands':
            self.hands = value
        elif string == 'trunk':
            self.trunk = value
        elif string == 'legs':
            self.legs = value
        elif string == 'feet':
            self.feet = value
        elif string == 'right_hand':
            self.right_hand = value
        elif string == 'left_hand':
            self.left_hand = value
        else:
            print("Cette partie n'est pas connue")


class BagPack:

    def __init__(self):
        self.potions = []
        self.weapons = []
        self.armors = []
        self.jewelries = []
        self.useless_Objects = []

    def addItem(self, item):
        if type(item) == Weapon:
            self.weapons += [item]
        elif type(item) == Armor:
            self.armors += [item]
        elif type(item) == Jewelry:
            self.jewelries += [item]
        elif type(item) == Potion:
            self.potion += [item]
        else:
            self.useless_Objects += [item]

    def removeItem(self, item):
        

e = Equipment()
print(e.equip(0, e.head))
