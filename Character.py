from AttributeSet import *
from CompetenceSet import *
from Organisation import *


class Character:

    """
    A class for Characters.
    Parameters :
        - id (Integer)
        - name (String)
        - race (String)
        - attributes set (Instance of AttributeSet)
        - competences set (Instance of CompetenceSet)
        - mystery Value (Integer [0,10])
        - blood thirst Value (Integer [0,10])
        - level of greed (Integer [0,10])
        - gold (Integer)
        - relations (Dictionnary of Integer)
        - RACE_RELATIONS (Dictionnary of Integer)
        - Location (Instance of Location)
    """

    def __init__(self, idChar, name, race, attributes, competences,
                 mystery, blood_thirst, greed_lvl, gold, relations):
        self.idChar = idChar                            # Integer
        self.name = name                                # String
        self.race = race                                # String
        self.attributes = attributes                    # AttributeSet
        self.competences = competences                  # CompetenceSet
        self.mystery = mystery                          # Integer [0,10]
        self.blood_thirst = blood_thirst                # Integer [0,10]
        self.greed_lvl = greed_lvl                      # Integer [0,10]
        self.gold = gold                                # Integer
        self.relations = relations                      # Dictionnary
        self.RACE_RELATIONS = self.raceRelations()      # Dictionnary
        self.location = 'Sommet du graphe de carte'     # String (by now)

    def screen(self):
        """
        Print readable informations.
        - output : String
        """
        return("Je m'appelle {}".format(self.name))

    def raceRelations(self):
        """
        Create RACE_RELATIONS.
        - output : RACE_RELATIONS
        """
        if self.race == 'humain':
            return({'humain': -5})

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

    def questRequest(self, quest, team):
        """
        Add a quest in waiting quest list of team.
        - output : None
        """
        print("{} vous propose une quete a l'equipe {}"
              .format(self.name, team.name))
        team.addWaitingQuest(quest)

    def createTeam(self, name, description):
        """
        Create a new team and upgrade the player to TeamChief.
        - output : None
        """
        chief = TeamChief(self.idChar, self.name, self.race, self.attributes,
                          self.competences, self.mystery,
                          self.blood_thirst, self.greed_lvl,
                          self.gold, self.relations)
        del self
        return(Team(name, chief, [chief], 0, description))


class TeamChief(Character):

    """
    Class for the team chief.
    Parameters :
        - id (Integer)
        - name (String)
        - race (String)
        - attributes set (Instance of AttributeSet)
        - competences set (Instance of CompetenceSet)
        - mystery Value (Integer [0,10])
        - blood thirst Value (Integer [0,10])
        - level of greed (Integer [0,10])
        - gold (Integer)
        - relations (Dictionnary of Integer)
        - RACE_RELATIONS (Dictionnary of Integer)
        - Location (Instance of Location)
    """

    def __init__(self, idChar, name, race, attributes, competences,
                 mystery, blood_thirst, greed_lvl, gold, relations):
        Character.__init__(self, idChar, name, race, attributes, competences,
                           mystery, blood_thirst, greed_lvl, gold, relations)

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
            print("Cette quete n'est pas dans les quetes en attente")

    def refuseQuestRequest(self, quest, team):
        """
        Reject a quest (from waiting quests)
        - output : None
        """
        try:
            team.waiting_Quest.remove(quest)
        except ValueError:
            print("Cette quete n'est pas dans les quetes en attente")
