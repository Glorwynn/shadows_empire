from AttributeSet import *
from CompetenceSet import *
from Organisation import *
from Equipment import *
from Race import *
from Quest import *
from Location import *
from Building import *


class Character:

    """
        A class for Characters.
        =======================
        Attributes :
        ------------
            - id: Integer
            - name: String
            - race: String
            - attributes set: Instance of AttributeSet - copy from race
            - competences set: Instance of CompetenceSet - copy from race
            - mystery Value: Integer [0,10]
            - blood thirst Value: Integer [0,10]
            - level of greed: Integer [0,10]
            - gold: Integer
            - estate: List of buildings
            - equipment: Dictionnary of Item {Location: Item}
            - other objets: List of Item {Item: number}
            - Bonus: Dictionnary of Integer
            - relations: Dictionnary of Integer
            - RACE_RELATIONS: Dictionnary of Integer - copy from race
            - Location: Instance of Location
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
        self.estates = []                                # List of Building
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
            ----------------------------
            The formula is: ...

            OUTPUT: Integer
        """
        at_blth = (self.attributes.attractivity + self.blood_thirst)/4
        if at_blth == 0:
            return 0
        else:
            bonus_myst = self.mystery*(4/10)
            return(int((at_blth + (bonus_myst)/2)))

    def getObedience(self, character):
        """
            Compute the obedience value of a character.
            -------------------------------------------
            The formula is: ...

            OUTPUT: Integer
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
            Compute the loyalty value of a character.
            -----------------------------------------
            The formula is: ...

            OUTPUT : Integer
        """
        return(self.getObedience(character) + (self.greed_lvl - 5))

    def getStress(self):
        """
            Compute the stress value in the current location.
            -------------------------------------------------
            The formula is: ...

            OUTPUT : Integer
        """
        return(self.RACE_RELATIONS[self.location.people.name]/2)

    ##########################
    # Fonctions de deplacement
    ##########################

    def moveTo(self, location):
        """
            Move to new Location.
            ---------------------

            OUTPUT: None
        """
        self.location = location

    ###########################
    # Fonctions pour les objets
    ###########################

    def takeItem(self, item, number=1):
        """
            Add an item to BagPack
            ----------------------

            OUTPUT: None
        """
        self.bagpack.addItem(item, number)

    def putItem(self, item, number=1):
        """
            Remove an item from bagpack
            ---------------------------

            OUTPUT: None
        """
        self.bagpack.removeItem(item, number)

    def equipWeapon(self, weapon, hand="right_hand"):
        """
            Equip a weapon.
            ---------------
            Add a weapon from bagpack to equipment and apply enchantments
            on the character.

            OUTPUT: None
        """
        if weapon in self.bagpack.weapons:
            self.equipment.addWeapon(weapon, hand)
            self.putItem(weapon)
            weapon.equipEffect(self)
        else:
            print("Vous ne possedez pas cet objet")

    def unequipWeapon(self, hand="all"):
        """
            Unequip a weapon.
            -----------------
            Add a weapon from equipment to bagpack and disapply enchantments.

            OUTPUT: None
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
            Equip an armor.
            ---------------
            Add an armor from bagpack to equipment and apply enchantments
            on the character.

            OUTPUT: None
        """
        if armor in self.bagpack.armors:
            self.equipment.addArmor(armor)
            self.putItem(armor)
            armor.equipEffect(self)
        else:
            print("Vous ne possedez pas cet objet")

    def unequipArmor(self, location="all"):
        """
            Unequip an armor.
            -----------------
            Add an armor from equipment to bagpack and disapply enchantments.

            OUTPUT: None
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
            Equip a jewelry.
            ---------------
            Add a jewelry from bagpack to equipment and apply enchantments
            on the character.

            OUTPUT: None
        """
        if jewelry in self.bagpack.jewelries:
            self.equipment.addJewelry(jewelry, finger)
            self.putItem(jewelry)
            jewelry.equipEffect(self)
        else:
            print("Vous ne possedez pas cet objet")

    def unequipJewelry(self, location="all"):
        """
            Unequip a jewelry.
            -----------------
            Add a jewelry from equipment to bagpack and disapply enchantments.

            OUTPUT: None
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
            The character make a quest request to a team.
            ---------------------------------------------
            Add the quest to the list of waiting quests

            OUTPUT: None
        """
        print("{} vous propose une quete a l'equipe {}"
              .format(self.name, team.name))
        team.waiting_Quest += [quest]

    ##########################
    # Fonctions d'organisation
    ##########################

    def createTeam(self, name, description):
        """
            Create a new Team
            -----------------
            Upgrade the character to TeamChief and create a new team
            which the caracter is the chief

            OUTPUT: None
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
        ======================
        Attributes:
        -----------
            - id: Integer
            - name: String
            - race: String
            - attributes set: Instance of AttributeSet - copy from race
            - competences set: Instance of CompetenceSet - copy from race
            - mystery Value: Integer [0,10]
            - blood thirst Value: Integer [0,10]
            - level of greed: Integer [0,10]
            - gold: Integer
            - equipment: Dictionnary of Item {Location: Item}
            - other objets: List of Item {Item: number}
            - Bonus: Dictionnary of Integer
            - relations: Dictionnary of Integer
            - RACE_RELATIONS: Dictionnary of Integer - copy from race
            - Location: Instance of Location
    """

    def __init__(self, idChar, name, race, HP, attributes, competences,
                 mystery, blood_thirst, greed_lvl, gold, relations, team):
        Character.__init__(self, idChar, name, race, HP, attributes,
                           competences, mystery, blood_thirst,
                           greed_lvl, gold, relations)
        self.team = team

    def enroll(self, character):
        """
            Enroll a character in the chief team
            -------------------------------------
            Add character in the member list if there is enough places

            OUTPUT: None
        """
        if self.idChar == team.chief.idChar:
            if len(team.members) < 4:
                team.members += [character]
                character.greed_lvl += ENROLL_CHARACTER_GREED
            else:
                print("Il y a deja trop de personnes dans cette equipe")
        else:
            print("Vous n'etes pas chef de cette equipe")

    def fire(self, character, team):
        """
            Fire a Character of the team
            ----------------------------
            Remove a character from the member list

            OUTPUT: None
        """
        if self.idChar == team.chief.idChar:
            try:
                team.members.remove(character)
                character.greed_lvl += FIRE_CHARACTER_GREED
            except ValueError:
                print(character.name +
                      " n'est pas dans les membre de l'equipe " +
                      team.name)
        else:
            print("Vous n'etes pas chef de cette equipe")

    def acceptQuestRequest(self, quest, team):
        """
            Accept a quest.
            ---------------
            Add quest from Waiting quests to quest queue.

            OUTPUT: None
        """
        try:
            team.waiting_Quest.remove(quest)
            team.quest_Queue += [quest]
        except ValueError:
            print("Cette quete ne vous a pas ete proposee")

    def refuseQuestRequest(self, quest, team):
        """
            Reject a quest.
            ---------------
            Remove the quest from waiting quests.

            OUTPUT: None
        """
        try:
            team.waiting_Quest.remove(quest)
            quest.giver.greed_lvl += REFUSEQUESTREQUEST_GIVER_GREED
        except ValueError:
            print("Cette quete ne vous a pas ete proposee")
