class Quest:

    """
    Class for generic quests.
    Parameters :
        - Title (String)
        - target (Character, Team or Organisation)
        - reward (gold, Character, Team, ???)
        - level (Integer [0,20])
        - location (Location)
        - duration (Integer)
    """

    def __init__(self, title, target, reward,
                 level, location, duration):
        self.title = title
        self.target = target
        self.reward = reward
        self.level = level
        self.location = location
        self.duration = duration


class StealQuest(Quest):

    """
    Class for steal quests.
    Parameters :
        - Title (String)
        - target (Character, Team or Organisation)
        - reward (gold, Character, Team, ???)
        - level (Integer [0,20])
        - location (Location)
        - duration (Integer)
        - object to steal (Object)
    """

    def __init__(self, title, target, reward,
                 level, location, duration, object_to_steal):
        Quest.__init__(self, title, target, reward,
                       level, location, duration)
        self.object_to_steal = object_to_steal
