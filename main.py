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
# - Equiper une arme + application de l'enchantement
# - Déséquiper une arme + suppression de l'enchantement
# - Equiper une armure + application de l'enchantement
# - Déséquiper une armure + suppression de l'enchantement
# - Equiper un bijou + application de l'enchantement
# - Déséquiper un bijou + suppression de l'enchantement

humain = Race('humain',
              AttributeSet(20, 10, 0, 0, 0, 0, 10, 0),
              CompetenceSet(2, 2, 2),
              {'Humain': 10})

gloglo = Character(1, 'Glorwynn', humain,
                   10, 10, 5, 10, {})

toto = Character(1, 'Toto', humain,
                 10, 10, 5, 10, {})

e1 = Effect('1', 'HP+', "HP", 10, 0)
e2 = Effect('2', 'rage+', "rage", 5, 0)
w1 = Weapon('arme1', 0, 0, [e1, e2], 0, 11, 'onehand')
w2 = Weapon('arme2', 0, 0, [e1], 0, 11, 'onehand')
a1 = Armor('Casque', 0, 0, [e1], 0, 11, 'head')
a2 = Armor('Jambes', 0, 0, [e2], 0, 11, 'legs')
j1 = Jewelry('Doigt', 0, 0, [e1], 0, 'ring')
j2 = Jewelry('Cou', 0, 0, [], 0, 'necklace')
q1 = StealQuest('Quete1', toto, 10, 0, 'loc', 0, w2)

print(help(Character))