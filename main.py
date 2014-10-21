from Character import *
from AttributeSet import *
from CompetenceSet import *
from Organisation import *
from Quest import *

attributes_gloglo = AttributeSet(0, 0, 0, 0, 10, 0)
competences_gloglo = CompetenceSet(2, 2, 2)
attributes_toto = AttributeSet(5, 5, 5, 5, 5, 5)
competences_toto = CompetenceSet(1, 1, 1)

gloglo = Character('Glorwynn', 'humain', attributes_gloglo, competences_gloglo,
                   10, 10, 5, 10,
                   {'Toto': 3})

toto = Character('Toto', 'humain', attributes_toto,
                 competences_toto, 5, 5, 0, 10, {'Glowynn': 3})

team = Team('equipe1', gloglo, [gloglo], 0, '')
miss = StealQuest('mission1', 'cible', 10, 20, 0, team, 0, 'objet')
team.addQuest(miss)
print(team.questSuccessRate(team.nextQuest()))
team.doingQuest(team.nextQuest())
print(gloglo.gold)
print(len(team.quest_Queue))
