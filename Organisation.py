from random import *


class Organisation:
    def __init__(self, name, chief, teams, influence, description):
        self.name = name
        self.chief = chief
        self.teams = teams
        self.influence = influence
        self.description = description


class Team:
    def __init__(self, name, chief, members, satifaction, description):
        self.name = name
        self.chief = chief
        self.members = members
        self.quest_Queue = []
        self.satifaction = satifaction
        self.description = description
        self.maxMembers = 4

    def addMember(self, character):
        if len(self.members) >= 4:
            print("Il y a deja trop de personnes dans cette equipe")
        else:
            self.members += character

    def delMember(self, character):
        try:
            self.members.remove(character)
        except ValueError:
            print(character +
                  " n'est pas dans les membre de l'equipe " +
                  self.name)

    def addQuest(self, quest):
        self.quest_Queue += [quest]

    def nextQuest(self):
        return(self.quest_Queue[0])

    def goldDistribution(self, gold):
        for char in self.members:
            char.gold += gold/len(self.members)
        self.chief.gold += gold % len(self.members)

    def questTeamBonus(self, quest):
        char_level_effect = 0
        for char in self.members:
            char_level_effect += (char.competences.stealLevel() - quest.level)
        return char_level_effect

    def questSuccessRate(self, quest):
        return((100 - quest.level*4.9 + self.questTeamBonus(quest)))

    def doingQuest(self, quest):
        if (randint(1, 101) <= self.questSuccessRate(quest)):
            self.goldDistribution(quest.reward)
        else:
            print("Mission failed")
        self.quest_Queue = self.quest_Queue[1:]
