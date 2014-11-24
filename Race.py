from AttributeSet import *
from CompetenceSet import *


class Race:

    """
        Class for Races
        ===============
        Attributes:
            - name: String
            - attribute_set: AttributeSet
            - competence_set: CompetenceSet
            - relations: Dictionnary {race: value}
    """

    def __init__(self, name, attribute_set, competence_set, relations):
        self.name = name
        self.attribute_set = attribute_set
        self.competence_set = competence_set
        self.relations = relations
