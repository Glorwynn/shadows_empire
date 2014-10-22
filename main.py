from Character import *
from AttributeSet import *
from CompetenceSet import *
from Organisation import *
from Quest import *

# Actions fonctionnelles :
# - Calcule de la valeur d'infuence d'un personnage
# - Calcule de la valeur d'obéissance d'un personnage
# - Calcule de la valeur de loyauté d'un personnage
# - calcule du niveau de vol d'un personnage
# - créer une équipe
# - ajouter un membre d'une équipe
# - supprimer un membre d'une équipe
# - Proposer une quete
# - Accepter un quete
# - Refuser une quete
# - sélectionner la quete suiante de l'équipe
# - Bonus de l'équipe sur la quete
# - Pourcentage de réussite de l'équipe pour la quete
# - effectuer une quete

attributes_gloglo = AttributeSet(0, 0, 0, 0, 10, 0)
competences_gloglo = CompetenceSet(2, 2, 2)
attributes_toto = AttributeSet(5, 5, 5, 5, 5, 5)
competences_toto = CompetenceSet(1, 1, 1)
attributes_toto = AttributeSet(5, 5, 5, 5, 5, 5)
competences_toto = CompetenceSet(1, 1, 1)

gloglo = TeamChief(1, 'Glorwynn', 'humain', attributes_gloglo,
                   competences_gloglo,
                   10, 10, 5, 10,
                   {'Toto': 3})

toto = Character(2, 'Toto', 'humain', attributes_toto,
                 competences_toto, 5, 5, 0, 10, {'Glowynn': 3})

titi = Character(3, 'Titi', 'humain', attributes_toto,
                 competences_toto, 5, 5, 0, 10, {'Glowynn': 3})

team = gloglo.createTeam('Mon Equipe', '')
gloglo.addMember(toto, team)
print(team.screenMembers())
quest = StealQuest('mission1', 'cible', 10, 20, 0, 0, 'objet')
quest2 = StealQuest('mission1', 'cible', 10, 20, 0, 0, 'objet')
titi.questRequest(quest, team)
gloglo.refuseQuestRequest(quest, team)
print(team.quest_Queue)
print(help(Character))
