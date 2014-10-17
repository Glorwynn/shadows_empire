class AttributeSet:
    """docstring for AttributeSet"""
    def __init__(self, constitution, agility, esprit, sensitivity,
                 attractivity, rage):
        self.constitution = constitution
        self.agility = agility
        self.esprit = esprit
        self.sensitivity = sensitivity
        self.attractivity = attractivity
        self.rage = rage

    def __repr__(self):
        return("Constitution: {}\n"
               "Agility: {}\n"
               "Esprit: {}\n"
               "Sensitivity: {}\n"
               "Attractivity: {}\n"
               "Rage: {}\n")
