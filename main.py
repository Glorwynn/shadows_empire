from Character import *
from Quest import *


# Actions fonctionnelles :
# - Calcule de la valeur d'infuence d'un personnage
# - Calcule de la valeur d'obeissance d'un personnage
# - Calcule de la valeur de loyaute d'un personnage
# - calcule du niveau de vol d'un personnage
# - creer une equipe
# - ajouter un membre d'une equipe
# - supprimer un membre d'une equipe
# - Proposer une quete
# - Accepter un quete
# - Refuser une quete
# - selectionner la quete suiante de l'equipe
# - Bonus de l'equipe sur la quete
# - Pourcentage de reussite de l'equipe pour la quete
# - effectuer une quete
# - Ajouter un objet dans l'inventaire
# - Supprimer un objet de l'inventaire
# - Equiper une arme
# - Déséquiper une arme
# - Equiper une armure
# - Déséquiper une armure
# - Equiper un bijou
# - Déséquiper un bijou

gloglo = Character(1, 'Glorwynn', 'humain', 20,
                   AttributeSet(0, 0, 0, 0, 10, 0),
                   CompetenceSet(2, 2, 2),
                   10, 10, 5, 10,
                   {'Toto': 3})

toto = Character(1, 'Toto', 'humain', 20,
                 AttributeSet(0, 0, 0, 0, 10, 0),
                 CompetenceSet(2, 2, 2),
                 10, 10, 5, 10,
                 {'Toto': 3})

team = gloglo.createTeam("Team", '')
print(isinstance(team.chief, TeamChief))

w1 = Weapon('arme', 0, 0, [], 0, 11, 'onehand')
w2 = Weapon('arme2', 0, 0, [], 0, 11, 'onehand')
a1 = Armor('Casque', 0, 0, [], 0, 11, 'head')
a2 = Armor('Jambes', 0, 0, [], 0, 11, 'legs')
j1 = Jewelry('Doigt', 0, 0, [], 0, 'ring')
j2 = Jewelry('Cou', 0, 0, [], 0, 'necklace')
q1 = StealQuest('Quete1', toto, 10, 0, 'loc', 0, w2)

toto.questRequest(q1, team)
print(team.waiting_Quest[0].title)
team.chief.acceptQuestRequest(q1, team)
print(team.doingQuest(q1))

gloglo.takeItem(w1, 4)
gloglo.takeItem(w2, 4)
gloglo.takeItem(a1, 3)
gloglo.takeItem(a2, 3)
gloglo.takeItem(j1, 2)
gloglo.takeItem(j2, 2)

print(gloglo.attributes.rage)