import math

class Character:
    """A class for Characters."""
    def __init__(self, name, race, constitution, agility, esprit, sensitivity, attractness, rage, mystery, blood_thirst, greed_lvl, relations):
        self.name = name                                # String
        self.race = race                                # String
        self.constitution = constitution                # Integer [0,10]
        self.agility = agility                          # Integer [0,10]
        self.esprit = esprit                            # Integer [0,10]
        self.sensitivity = sensitivity                  # Integer [0,10]
        self.attractness = attractness                  # Integer [0,10]
        self.rage = rage                                # Integer [0,10]
        self.mystery = mystery                          # Integer [0,10]
        self.blood_thirst = blood_thirst                # Integer [0,10]
        self.greed_lvl = greed_lvl                      # Integer [0,10]
        self.relations = relations                      # Dictionnaire
        self.RACE_RELATIONS = self.getRaceRelations()   # Dictionnaire (A transformer en classe)

    def __repr__(self):
        return("Je m'appelle {}".format(self.name))

    def getRaceRelations(self):
        if self.race == 'humain':
            return({'humain': -5})

    def getInfluence(self):
        at_blth = (self.attractness + self.blood_thirst)/4 
        if at_blth == 0:
            return 0
        else:
            bonus_myst = self.mystery*(4/10)
            return(int((at_blth + (bonus_myst)/2)))

    def getObedience(self, character):
        influence = character.getInfluence()
        if self.RACE_RELATIONS[character.race] <= -5:
            return(int(self.RACE_RELATIONS[character.race] + influence))
        elif self.RACE_RELATIONS[character.race] > -5 and self.RACE_RELATIONS[character.race] <= 0:
            return(int(self.RACE_RELATIONS[character.race] + influence/1.3))
        elif self.RACE_RELATIONS[character.race] > 0 and self.RACE_RELATIONS[character.race] <= 5:
            return(int(self.RACE_RELATIONS[character.race] + influence/2))
        else:
            return(int(self.RACE_RELATIONS[character.race] + influence/3))

    def getLoyalty(self, character):
        return(self.getObedience(character) + (self.greed_lvl - 5))

