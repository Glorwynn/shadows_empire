from random import *


class Organisation:

    """
        Class for Organisation
        ======================
        Parameters :
        ------------
            - name: String
            - chief: Character
            - members: List of Character
            - description: String
    """

    def __init__(self, name, chief, members, influence, description):
        self.name = name
        self.chief = chief
        self.members = members
        self.description = description

    def getInfluence(self):
        """
            Compute the influence value of the Organisation
            -----------------------------------------------
            The formula is: ...

            OUTPUT: Integer
        """
        sum_Influence = 0
        for char in self.members:
            sum_Influence += char.getInfluence()
        value = (2*chief.getInfluence() + sum_Influence) / len(self.members)
        return(int(value))


class Team:

    """
    Class for Team.
    Parameters :
        - name: String
        - chief: Character
        - members: List of Character
        - waiting_Quest: List of Quest
        - quest_Queue: List of Quest
        - satifaction: Integer
        - description: String
        - maxMembers: Integer
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

    def goldDistribution(self, gold):
        """
            Distribute the reward in the team
            ---------------------------------
            Same share for all member (including the chief),
            and the remaining gold for the chief

            OUTPUT: None
        """
        for char in self.members:
            char.gold += gold/(len(self.members)+1)
        self.chief.gold += gold % len(self.members)

    def questTeamBonus(self, quest):
        """
            Compute the Bonus/Malus of the team for a quest
            -----------------------------------------------
            The formula is: 
                sum of characters differences from the quest level

            OUTPUT: Integer
        """
        char_level_effect = 0
        for char in self.members:
            char_level_effect += (char.competences.stealLevel() - quest.level)
        return char_level_effect

    def questSuccessRate(self, quest):
        """
            Compute the success rate of the team for a quest
            ------------------------------------------------

            OUTPUT: Float
        """
        return((100 - quest.level*4.9 + self.questTeamBonus(quest)))

    def doingQuest(self, quest):
        """
            Doing a quest
            -------------
            The team do the quest and, in case of success,
            distribute the reward and the greed bonus/malus.

            OUTPUT: None
        """
        if (randint(1, 101) <= self.questSuccessRate(quest)):
            self.goldDistribution(quest.reward)
            quest.giver.greed_lvl += DOINGQUEST_WIN_GIVER_GREED
            for character in self.members:
                character.greed_lvl += DOINGQUEST_WIN_TEAM_GREED
        else:
            print("Mission failed")
            quest.giver.greed_lvl += DOINGQUEST_FAIL_GIVER_GREED
            for character in self.members:
                character.greed_lvl += DOINGQUEST_FAIL_TEAM_GREED
        self.quest_Queue = self.quest_Queue[1:]
