class CompetenceSet:
    def __init__(self, furtivity, stealing, lockpicking):
        self.furtivity = furtivity
        self.stealing = stealing
        self.lockpicking = lockpicking

    def __repr__(self):
        return("Furtivite : {}\n".format(self.furtivity) +
               "Stealing : {}\n".format(self.stealing) +
               "Lockpicking : {}".format(self.stealing))

    def upgrade(self, competence, value):
        competence += value

    def downgrade(self, competence, value):
        competence -= value

    def stealLevel(self):
        return((self.furtivity + self.stealing + self.lockpicking)/3)
