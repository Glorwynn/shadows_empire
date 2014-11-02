from Character import *
from AttributeSet import *
from CompetenceSet import *
from Organisation import *
from Quest import *
from Object import *

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

attributes_gloglo = AttributeSet(0, 0, 0, 0, 10, 0)
competences_gloglo = CompetenceSet(2, 2, 2)
attributes_toto = AttributeSet(5, 5, 5, 5, 5, 5)
competences_toto = CompetenceSet(1, 1, 1)

potion = Potion(1, 'potion', 10, 100,
                [Effect(1, '', 'furtivity', 10, 0),
                 Effect(2, '', 'stealing', 5, 0)])

gloglo = Character(1, 'Glorwynn', 'humain', 20, attributes_gloglo,
                   competences_gloglo,
                   10, 10, 5, 10,
                   {"head": None},
                   {potion},
                   {'Toto': 3})

toto = Character(2, 'Toto', 'humain', 20, attributes_toto,
                 competences_toto,
                 5, 5, 0, 10,
                 {"head": None},
                 {},
                 {'Glowynn': 3})

titi = Character(3, 'Titi', 'humain', 20, attributes_toto,
                 competences_toto,
                 5, 5, 0, 10,
                 {"head": None},
                 {},
                 {'Glowynn': 3})

quest = StealQuest('mission1', 'cible', 10, 20, 0, 0, 'objet')
quest2 = StealQuest('mission1', 'cible', 10, 20, 0, 0, 'objet')
w = Weapon('arme', 0, 0, [], 0, 11, 10, 'onehand')
a = Armor('Casque', 0, 0, [], 0, 11, 10, 'head')
gloglo.bagpack.addItem(w)


# print(gloglo.competences.furtivity, gloglo.competences.stealing)
# potion.actEffect(gloglo)
# print(gloglo.competences.furtivity, gloglo.competences.stealing)