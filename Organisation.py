class Organisation:
    def __init__(self, name, chief, teams, influence, description):
        self.name = name
        self.chief = chief
        self.teams = teams
        self.influence = influence
        self.description = description


class Team:
    def __init__(self, name, members, satifaction, description):
        self.name = name
        self.members = members
        self.satifaction = satifaction
        self.description = description
        self.maxMembers = 4

    def addMember(self, character):
        self.members += character

    def delMember(self, character):
        try:
            self.members.remove(character)
        except ValueError:
            print(character +
                  " n'est pas dans les membre de l'equipe " +
                  self.name)
