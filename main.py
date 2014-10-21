from Character import *
from AttributeSet import *
from CompetenceSet import *
from Organisation import *
from Mission import *

attributes_gloglo = AttributeSet(0, 0, 0, 0, 10, 0)
competences_gloglo = CompetenceSet(6, 4, 2)
attributes_toto = AttributeSet(5, 5, 5, 5, 5, 5)
competences_toto = CompetenceSet(1, 1, 1)

gloglo = Character('Glorwynn', 'humain', attributes_gloglo, competences_gloglo,
                   10, 10, 5,
                   {'Toto': 3})

toto = Character('Toto', 'humain', attributes_toto,
                 competences_toto, 5, 5, 0, {'Glowynn': 3})

team = Team('team1', [gloglo, toto], 2, '')
org = Organisation('Comp1', gloglo, team, 10, '')
miss = StealMission('mission1', 'cible', 10, 2, 6, team, 10, 'objet')
print(miss.successRate())
