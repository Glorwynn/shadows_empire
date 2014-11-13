from AttributeSet import *
from CompetenceSet import *
from Organisation import *
from Equipment import *
from Race import *
from Quest import *
from Location import *


class Character:

    """
    A class for Characters.
    Parameters :
        - id (Integer)
        - name (String)
        - race (String)
        - attributes set (Instance of AttributeSet - copy from race)
        - competences set (Instance of CompetenceSet - copy from race)
        - mystery Value (Integer [0,10])
        - blood thirst Value (Integer [0,10])
        - level of greed (Integer [0,10])
        - gold (Integer)
        - equipment (Dictionnary of Objects= Location: Object)
        - other objets (List of Objects= Object: number)
        - Bonus (Dictionnary of Integer)
        - relations (Dictionnary of Integer)
        - RACE_RELATIONS (Dictionnary of Integer - copy from race)
        - Location (Instance of Location)
    """

    def __init__(self, idChar, name, race, mystery, blood_thirst,
                 greed_lvl, gold, relations, location):
        self.idChar = idChar                            # Integer
        self.name = name                                # String
        self.race = race                                # String
        self.attributes = race.attribute_set            # AttributeSet
        self.competences = race.competence_set          # CompetenceSet
        self.mystery = mystery                          # Integer [0,10]
        self.blood_thirst = blood_thirst                # Integer [0,10]
        self.greed_lvl = greed_lvl                      # Integer [0,10]
        self.gold = gold                                # Integer
        self.equipment = Equipment()                    # Equipment
        self.bagpack = BagPack()                        # BagPack
        self.relations = relations                      # Dictionnary
        self.RACE_RELATIONS = race.relations            # Dictionnary
        self.location = location                        # String (by now)

    #############################################
    # Definitions des relations entre personnages
    #############################################

    def getInfluence(self):
        """
        Compute the influence value.
        - output : Integer
        """
        at_blth = (self.attributes.attractivity + self.blood_thirst)/4
        if at_blth == 0:
            return 0
        else:
            bonus_myst = self.mystery*(4/10)
            return(int((at_blth + (bonus_myst)/2)))

    def getObedience(self, character):
        """
        Compute the obedience value.
        - output : Integer
        """
        influence = character.getInfluence()
        if self.RACE_RELATIONS[character.race] <= -5:
            return(int(self.RACE_RELATIONS[character.race] + influence))
        elif (self.RACE_RELATIONS[character.race] > -5
              and self.RACE_RELATIONS[character.race] <= 0):
            return(int(self.RACE_RELATIONS[character.race] + influence/1.3))
        elif (self.RACE_RELATIONS[character.race] > 0
              and self.RACE_RELATIONS[character.race] <= 5):
            return(int(self.RACE_RELATIONS[character.race] + influence/2))
        else:
            return(int(self.RACE_RELATIONS[character.race] + influence/3))

    def getLoyalty(self, character):
        """
        Compute the loyalty value.
        - output : Integer
        """
        return(self.getObedience(character) + (self.greed_lvl - 5))

    def getStress(self):
        return(self.RACE_RELATIONS[self.location.people.name]/2)

    ##########################
    # Fonctions de deplacement
    ##########################

    def goToLocaction(self, location):
        self.location = location

    ###########################
    # Fonctions pour les objets
    ###########################

    def takeItem(self, item, number=1):
        """
        Add an item in BagPack
        - output: None
        """
        self.bagpack.addItem(item, number)

    def putItem(self, item, number=1):
        """
        Remove an item from bagpack
        - output: None
        """
        self.bagpack.removeItem(item, number)

    def equipWeapon(self, weapon, hand="right_hand"):
        """
        Equip a weapon. Add the weapon in the equipment, remove it from
        the bagpack (if it possible) and apply the effects of it
        on the character.
        - output: None
        """
        if weapon in self.bagpack.weapons:
            self.equipment.addWeapon(weapon, hand)
            self.putItem(weapon)
            weapon.equipEffect(self)
        else:
            print("Vous ne possedez pas cet objet")

    def unequipWeapon(self, hand="all"):
        """
        Unequip a weapon. Remove the weapon from the equipment
        (if it possible), add it in the bagpack and disapply the effects
        of it on the character.
        - output: None
        """
        weapons = {'right_hand': self.equipment.right_hand,
                   'left_hand': self.equipment.left_hand}
        if hand == 'all':
            for w in weapons:
                self.takeItem(weapons[w])
                weapons[w].unequipEffect(self)
                self.equipment.removeArmor(w)
        else:
            try:
                self.takeItem(weapons[hand])
                weapons[hand].unequipEffect(self)
                self.equipment.removeWeapon(hand)
            except KeyError:
                print("Emplacement invalide")
            except AttributeError:
                print("Il n'y a rien a cet emplacement")

    def equipArmor(self, armor):
        """
        Equip an armor. Add the armor in the equipment, remove it from
        the bagpack (if it possible) and apply the effects of it
        on the character.
        - output: None
        """
        if armor in self.bagpack.armors:
            self.equipment.addArmor(armor)
            self.putItem(armor)
            armor.equipEffect(self)
        else:
            print("Vous ne possedez pas cet objet")

    def unequipArmor(self, location="all"):
        """
        Unequip an armor. Remove the armor from the equipment
        (if it possible), add it in the bagpack and disapply the effects
        of it on the character.
        - output: None
        """
        armors = {"head": self.equipment.head,
                  "shoulders": self.equipment.shoulders,
                  "arms": self.equipment.arms,
                  "trunk": self.equipment.trunk,
                  "legs": self.equipment.legs,
                  "feet": self.equipment.feet}
        if location == 'all':
            for armor in armors:
                self.takeItem(armors[armor])
                armors[armor].unequipEffect(self)
                self.equipment.removeArmor(armor)
        else:
            try:
                self.takeItem(armors[location])
                armors[location].unequipEffect(self)
                self.equipment.removeArmor(location)
            except KeyError:
                print("Emplacement invalide")
            except AttributeError:
                print("Il n'y a rien a cet emplacement")

    def equipJewelry(self, jewelry, finger='right1'):
        """
        Equip a jewelry. Add the jewelry in the equipment, remove it from
        the bagpack (if it possible) and apply the effects of it
        on the character.
        - output: None
        """
        if jewelry in self.bagpack.jewelries:
            self.equipment.addJewelry(jewelry, finger)
            self.putItem(jewelry)
            jewelry.equipEffect(self)
        else:
            print("Vous ne possedez pas cet objet")

    def unequipJewelry(self, location="all"):
        """
        Unequip a jewelry. Remove the jewelry from the equipment
        (if it possible), add it in the bagpack and disapply the effects
        of it on the character.
        - output: None
        """
        jewelries = {"right1": self.equipment.right1,
                     "right2": self.equipment.right2,
                     "left1": self.equipment.left1,
                     "left2": self.equipment.left2,
                     "neck": self.equipment.neck,
                     "wrist": self.equipment.wrist}
        if location == 'all':
            for j in jewelries:
                self.takeItem(jewelries[j])
                jewelries[j].unequipEffect(self)
                self.equipment.removeJewelry(j)
        else:
            try:
                self.takeItem(jewelries[location])
                jewelries[location].unequipEffect(self)
                self.equipment.removeJewelry(location)
            except KeyError:
                print("Emplacement invalide")
            except AttributeError:
                print("Il n'y a rien a cet emplacement")

    #####################
    # Fonctions de quetes
    #####################

    def questRequest(self, quest, team):
        """
        Add a quest in waiting quest list of team.
        - output : None
        """
        print("{} vous propose une quete a l'equipe {}"
              .format(self.name, team.name))
        team.waiting_Quest += [quest]

    ##########################
    # Fonctions d'organisation
    ##########################

    def createTeam(self, name, description):
        """
        Create a new team and upgrade the player to TeamChief.
        - output : None
        """
        chief = TeamChief(self.idChar, self.name, self.race, self.HP,
                          self.attributes, self.competences, self.mystery,
                          self.blood_thirst, self.greed_lvl,
                          self.gold, self.relations)
        del self
        return(Team(name, chief, [chief], 0, description))


class TeamChief(Character):

    """
    A class for TeamChief.
    Parameters :
        - id (Integer)
        - name (String)
        - race (String)
        - Health points (Integer)
        - attributes set (Instance of AttributeSet)
        - competences set (Instance of CompetenceSet)
        - mystery Value (Integer [0,10])
        - blood thirst Value (Integer [0,10])
        - level of greed (Integer [0,10])
        - gold (Integer)
        - equiped weapon / jewelry (Dictionnary of Objects= Location: Object)
        - other objets (List of Objects= Object: number)
        - relations (Dictionnary of Integer)
        - RACE_RELATIONS (Dictionnary of Integer)
        - Location (Instance of Location)
    """

    def __init__(self, idChar, name, race, HP, attributes, competences,
                 mystery, blood_thirst, greed_lvl, gold, relations):
        Character.__init__(self, idChar, name, race, HP, attributes,
                           competences, mystery, blood_thirst,
                           greed_lvl, gold, relations)

    def addMember(self, character, team):
        """
        Add a Character in the team
        - output : None
        """
        if self.idChar == team.chief.idChar:
            if len(team.members) < 4:
                team.members += [character]
            else:
                print("Il y a deja trop de personnes dans cette equipe")
        else:
            print("Vous n'etes pas chef de cette equipe")

    def delMember(self, character, team):
        """
        Delete a Character of the team
        - output : None
        """
        if self.idChar == team.chief.idChar:
            try:
                team.members.remove(character)
            except ValueError:
                print(character.name +
                      " n'est pas dans les membre de l'equipe " +
                      team.name)
        else:
            print("Vous n'etes pas chef de cette equipe")

    def acceptQuestRequest(self, quest, team):
        """
        Accept a quest (from waiting quests) and put it in quest_Queue
        - output : None
        """
        try:
            team.waiting_Quest.remove(quest)
            team.quest_Queue += [quest]
        except ValueError:
            print("Cette quete ne vous a pas ete proposee")

    def refuseQuestRequest(self, quest, team):
        """
        Reject a quest (from waiting quests)
        - output : None
        """
        try:
            team.waiting_Quest.remove(quest)
        except ValueError:
            print("Cette quete ne vous a pas ete proposee")
