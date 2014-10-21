class Mission:
    def __init__(self, title, target, reward,
                 difficulty, location, duration):
        self.title = title
        self.target = target
        self.reward = reward
        self.difficulty = difficulty
        self.location = location
        self.duration = duration


class StealMission(Mission):
    def __init__(self, title, target, reward,
                 difficulty, location, duration, object2steal):
        Mission.__init__(self, title, target, reward,
                         difficulty, location, duration)
        self.object2steal = object2steal


class ProstitutionMission(Mission):
    def __init__(self, title, target, reward,
                 difficulty, location, duration, dirtyness):
        Mission.__init__(self, title, target, reward,
                         difficulty, location, duration)
        self.dirtyness = dirtyness


class AssassinationMission(Mission):
    def __init__(self, title, target, reward,
                 difficulty, location, duration, procedure):
        Mission.__init__(self, title, target, reward,
                         difficulty, location, duration)
        self.procedure = procedure


class TraficMission(Mission):
    def __init__(self, title, target, reward,
                 difficulty, location, duration, article):
        Mission.__init__(self, title, target, reward,
                         difficulty, location, duration)
        self.article = article


class PirateMission(Mission):
    def __init__(self, title, target, reward,
                 difficulty, location, duration):
        Mission.__init__(self, title, target, reward,
                         difficulty, location, duration)
