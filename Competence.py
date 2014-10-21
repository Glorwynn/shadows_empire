class CompetenceSet:
    def __init__(self, furtivity, stealing, lockpicking):
        self.furtivity = furtivity
        self.stealing = stealing
        self.lockpicking = lockpicking

    def upgrade(self, competence, value):
        competence += value

    def downgrade(self, competence, value):
        competence -= value

    def stealLevel(self):
        return((self.furtivity + self.stealing + self.lockpicking)/3)

comp = CompetenceSet(2, 2, 2)
comp.upgrade(comp.furtivity, 1)
print(comp.furtivity)
