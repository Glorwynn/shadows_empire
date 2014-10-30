from AttributeSet import *
from Character import *


class Game:

    def __init__(self, difficulty):
        """ The class representing one game """
        self.dif = difficulty

    def makeHero(self):
        attributes_gloglo = AttributeSet(0, 0, 0, 0, 10, 0)

        gloglo = Character('Glorwynn', 'humain', attributes_gloglo,
                           10, 10, 5, {'Toto': 3})

    def makeSideKicks(self):
        attributes_toto = AttributeSet(5, 5, 5, 5, 5, 5)
        toto = Character('Toto', 'humain', attributes_toto,
                         5, 5, 0, {'Glowynn': 3})
