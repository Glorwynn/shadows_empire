# from CompetenceSet import *


class Character:
    RACE_RELATIONS = {'human': {'human': 5}, 'elf': {'human': -5}}

    """A class for Characters."""
    def __init__(self, name, race, attributes,
                 mystery, blood_thirst, greed_lvl, relations):
        self.name = name                                # String
        self.race = race                                # String
        self.attributes = attributes                    # AttributeSet
        self.mystery = mystery                          # Integer [0,10]
        self.blood_thirst = blood_thirst                # Integer [0,10]
        self.greed_lvl = greed_lvl                      # Integer [0,10]
        self.relations = relations                      # Dictionnary
        self.location = 'Sommet du graphe de carte'     # String (by now)

    def __repr__(self):
        return("Je m'appelle {}".format(self.name))
