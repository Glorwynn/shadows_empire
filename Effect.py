from Character import *


class Effect:
    """
        Class for effects and enchantments
        ==================================
        Attributes:
        -----------
            - idEffect: Integer
            - name: String
            - variable: String
            - value: Integer
    """

    def __init__(self, idEffect, name, variable, value, delay):
        # Peut etre ajouter les elements
        self.idEffect = idEffect
        self.name = name
        self.variable = variable
        self.value = value

    def apply(self, character):
        """
            Apply the effect on the character
            ---------------------------------

            OUTPUT: None
        """
        if self.variable == 'furtivity':
            character.competences.furtivity += self.value
        elif self.variable == 'stealing':
            character.competences.stealing += self.value
        elif self.variable == 'lockpicking':
            character.competences.lockpicking += self.value
        elif self.variable == 'HP':
            character.attributes.health_points += self.value
        elif self.variable == 'MP':
            character.attributes.mana_points += self.value
        elif self.variable == 'constitution':
            character.attributes.constitution += self.value
        elif self.variable == 'agility':
            character.attributes.agility += self.value
        elif self.variable == 'esprit':
            character.attributes.esprit += self.value
        elif self.variable == 'sensitivity':
            character.attributes.sensitivity += self.value
        elif self.variable == 'attractivity':
            character.attributes.attractivity += self.value
        elif self.variable == 'rage':
            character.attributes.rage += self.value
        elif self.my == 'mystery':
            character.mystery += self.value

    def disapply(self, character):
        """
            Disapply the effect on the character
            ------------------------------------

            OUTPUT: None
        """
        if self.variable == 'furtivity':
            character.competences.furtivity -= self.value
        elif self.variable == 'stealing':
            character.competences.stealing -= self.value
        elif self.variable == 'lockpicking':
            character.competences.lockpicking -= self.value
        elif self.variable == 'HP':
            character.attributes.health_points -= self.value
        elif self.variable == 'MP':
            character.attributes.mana_points -= self.value
        elif self.variable == 'constitution':
            character.attributes.constitution -= self.value
        elif self.variable == 'agility':
            character.attributes.agility -= self.value
        elif self.variable == 'esprit':
            character.attributes.esprit -= self.value
        elif self.variable == 'sensitivity':
            character.attributes.sensitivity -= self.value
        elif self.variable == 'attractivity':
            character.attributes.attractivity -= self.value
        elif self.variable == 'rage':
            character.attributes.rage -= self.value
        elif self.my == 'mystery':
            character.mystery -= self.value
