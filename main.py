from Character import *

gloglo = Character(
                'Glorwynn',     # Nom
                'humain',       # Race
                0,              # Carrure
                0,              # Adresse
                0,              # Esprit
                0,              # Sens
                10,             # Attraits
                0,              # Ravages
                10,             # Mystere
                10,             # Soif de sang
                5,              # Avidite
                {'Toto': 3}     # Relations
                )
toto = Character(
                'Toto',
                'humain',
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                0,
                {'Glowynn': 3}
                )

print(gloglo.getInfluence())
print(toto.getObedience(gloglo))
print(toto.getLoyalty(gloglo))