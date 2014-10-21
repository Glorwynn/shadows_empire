class Quest:
    def __init__(self, title, target, reward,
                 level, location, team, duration):
        self.title = title
        self.target = target
        self.reward = reward
        self.level = level
        self.location = location
        self.duration = duration
        self.team = team                 # Pour le modele minimal team = perso


class StealQuest(Quest):
    def __init__(self, title, target, reward,
                 level, location, team, duration, object2steal):
        Quest.__init__(self, title, target, reward,
                       level, location, team, duration)
        self.object2steal = object2steal
