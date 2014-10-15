from Character import *

gloglo = Character(
				'Glorwynn',	# Nom
				'humain',	# Race
				0,			# Carrure
				0,			# Adresse
				0,			# Esprit
				0,			# Sens
				10,			# Attraits
				0,			# Ravages
				10,			# Mystere
				10,			# Soif de sang
				5,			# Avidite
				{'Toto': 3}	# Relations
				)
toto = Character(
				'Toto',			# Nom
				'humain',		# Race
				5,				# Carrure
				5,				# Adresse
				5,				# Esprit
				5,				# Sens
				5,				# Attraits
				5,				# Ravages
				5,				# Mystere
				5,				# Soif de sang
				0,				# Avidite
				{'Glowynn': 3}	# Relations
				)

print(gloglo.getInfluence())
print(toto.getObedience(gloglo))
print(toto.getLoyalty(gloglo))