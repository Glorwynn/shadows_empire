class Mission:
    def __init__(self, title, target, reward,
                 level, location, team, duration):
        self.title = title
        self.target = target
        self.reward = reward
        self.level = level
        self.location = location
        self.duration = duration
        self.team = team


class StealMission(Mission):
    def __init__(self, title, target, reward,
                 level, location, team, duration, object2steal):
        Mission.__init__(self, title, target, reward,
                         level, location, duration)
        self.object2steal = object2steal

    def successRate(self):
        char_level_effect = 0
        for char in self.team:
            char_level_effect += (char.competences.stealLevel() - self.level)
        return char_level_effect


class ProstitutionMission(Mission):
    def __init__(self, title, target, reward,
                 level, location, team, duration, dirtyness):
        Mission.__init__(self, title, target, reward,
                         level, location, duration)
        self.dirtyness = dirtyness


class AssassinationMission(Mission):
    def __init__(self, title, target, reward,
                 level, location, team, duration, procedure):
        Mission.__init__(self, title, target, reward,
                         level, location, duration)
        self.procedure = procedure


class TraficMission(Mission):
    def __init__(self, title, target, reward,
                 level, location, team, duration, article):
        Mission.__init__(self, title, target, reward,
                         level, location, duration)
        self.article = article


class PirateMission(Mission):
    def __init__(self, title, target, reward,
                 level, location, team, duration):
        Mission.__init__(self, title, target, reward,
                         level, location, duration)
