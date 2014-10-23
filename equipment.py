from Object import *


class Equipment:

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

    def equip(self, item):
        if type(obj) == Weapon:
            self.right_hand = item
        elif type(obj) == Armor:
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
