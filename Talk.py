class Sentence:
    """docstring for Sentence"""
    def __init__(self, sentence):
        self.sentence = sentence


class BinaryQuestion(Sentence):
    """docstring for BinaryQuestion"""
    def __init__(self, sentence):
        Sentence.__init__(self, sentence)


class MultipleQuestions(Sentence):
    """docstring for MultipleQuestions"""
    def __init__(self, sentence, choices):
        Sentence.__init__(self, sentence)
        self.arg = arg