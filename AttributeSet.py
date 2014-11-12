class AttributeSet:
    """
    Class of attribut set of Characters
    Parameters :
        - constitution (Integer [0,10])
        - agility (Integer [0,10])
        - esprit (Integer [0,10])
        - sensitivity (Integer [0,10])
        - attractivity (Integer [0,10])
        - rage (Integer [0,10])
    """
    def __init__(self, constitution, agility, esprit, sensitivity,
                 attractivity, rage):
        self.constitution = constitution
        self.agility = agility
        self.esprit = esprit
        self.sensitivity = sensitivity
        self.attractivity = attractivity
        self.rage = rage

    def __repr__(self):
        return("Constitution: {}\n".format(self.constitution) +
               "Agility: {}\n".format(self.agility) +
               "Esprit: {}\n".format(self.esprit) +
               "Sensitivity: {}\n".format(self.sensitivity) +
               "Attractivity: {}\n".format(self.attractivity) +
               "Rage: {}\n".format(self.rage))
