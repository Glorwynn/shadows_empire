from random import *


class Organisation:

    """
    Class for Organisation
    Parameters :
        - name (String)
        - chief (Character)
        - members (List of Character)
        - description (String)
    """

    def __init__(self, name, chief, members, influence, description):
        self.name = name
        self.chief = chief
        self.members = members
        self.description = description

    def getInfluence(self):
        """
        Compute the influence value of the Organisation
        - output : integer
        """
        sum_Members_Influence = 0
        for char in self.members:
            sum_Influence += char.getInfluence()
        value = (chief.getInfluence() + sum_Influence) / len(self.members)
        return(int(value)


class Team:

    """
    Class for Team.
    Parameters :
        - name (String)
        - chief (Character)
        - members (List of Character)
        - waiting_Quest (List of Quest)
        - quest_Queue (List of Quest)
        - satifaction (Integer)
        - description (String)
    """

    def __init__(self, name, chief, members, satifaction, description):
        self.name = name
        self.chief = chief
        self.members = members
        self.waiting_Quest = []
        self.quest_Queue = []
        self.satifaction = satifaction
        self.description = description
        self.maxMembers = 4

    def screenMembers(self):
        """
        Print readable list of members
        - output : String
        """
        s = "["
        for char in self.members:
            s += char.name + ','
        return(s[:-1] + ']')

    def screen(self):
        """
        Print readable informations
        - output : String
        """
        return(
            "Nom : {}\n".format(self.name) +
            "Chef : {}\n".format(self.chief.name) +
            "Members : {}\n".format(self.screenMembers()) +
            "Quetes : {}\n".format(self.quest_Queue) +
            "Satisfaction : {}\n".format(self.satifaction) +
            "description : {}".format(self.description))
        return()

    def nextQuest(self):
        """
        Return the next quest in the queue
        - output : Quest
        """
        return(self.quest_Queue[0])

    def goldDistribution(self, gold):
        """
        Distribute the reward in the team (gold for now)
        - output : None
        """
        for char in self.members:
            char.gold += gold/len(self.members)
        self.chief.gold += gold % len(self.members)

    def questTeamBonus(self, quest):
        """
        Compute the Bonus/Malus of the team for a quest
        - output : Integer
        """
        char_level_effect = 0
        for char in self.members:
            char_level_effect += (char.competences.stealLevel() - quest.level)
        return char_level_effect

    def questSuccessRate(self, quest):
        """
        Compute the success rate of the team for a quest
        - output : Float
        """
        return((100 - quest.level*4.9 + self.questTeamBonus(quest)))

    def doingQuest(self, quest):
        """
        The team do the quest and, in case of success, distribute the reward
        - output : None
        """
        if (randint(1, 101) <= self.questSuccessRate(quest)):
            self.goldDistribution(quest.reward)
        else:
            print("Mission failed")
        self.quest_Queue = self.quest_Queue[1:]
