from Character import *
from AttributeSet import *

attributes_gloglo = AttributeSet(0, 0, 0, 0, 10, 0)
attributes_toto = AttributeSet(5, 5, 5, 5, 5, 5)

gloglo = Character('Glorwynn', 'humain', attributes_gloglo, 10, 10, 5,
                   {'Toto': 3})

toto = Character('Toto', 'humain', attributes_toto, 5, 5, 0, {'Glowynn': 3})

print(gloglo.getInfluence())
print(toto.getObedience(gloglo))
print(toto.getLoyalty(gloglo))
