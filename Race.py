from AttributeSet import *
from CompetenceSet import *


class Race:

    def __init__(self, name, attribute_set, competence_set, relations):
        self.name = name
        self.attribute_set = attribute_set
        self.competence_set = competence_set
        self.relations = relations
