class Attribute:

  """
    Class for Attribute
    ===================
    Attributes:
    -----------
        - id_Attribute: Integer
        - Name: String
  """

  def __init__(self, id_Attribute, name):
      self.id_Attribute = id_Attribute
      self.name = name


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

    def __init__(self, health_points, mana_points, constitution,
    agility, esprit, sensitivity, attractivity, rage):
    self.health_points = health_points
    self.mana_points = mana_points
    self.constitution = constitution
    self.agility = agility
    self.esprit = esprit
    self.sensitivity = sensitivity
    self.attractivity = attractivity
    self.rage = rage

    def __repr__(self):
    return("PV: {}\n".format(self.health_points) +
    "PM: {}\n".format(self.mana_points) +
    "Constitution: {}\n".format(self.constitution) +
    "Agility: {}\n".format(self.agility) +
    "Esprit: {}\n".format(self.esprit) +
    "Sensitivity: {}\n".format(self.sensitivity) +
    "Attractivity: {}\n".format(self.attractivity) +
    "Rage: {}\n".format(self.rage))
