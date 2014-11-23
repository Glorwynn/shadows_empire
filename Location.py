class Location:

    """
        Class for locations(map)
        ========================
        Attributes:
        -----------
            - name: String
            - envType: String
            - people: Dictionnary {race: rate}
            - nbPeople: Integer
            - size: Integer
    """

    def __init__(self, name, envType, people, population, size):
        self.name = name
        self.envType = envType
        self.people = people
        self.population = population
        self.size = size
