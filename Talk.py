class Sentence:

    """docstring for Sentence"""

    def __init__(self, sentence):
        self.sentence = sentence


class Question(Sentence):

    """docstring for BinaryQuestion"""

    def __init__(self, data):
        self.data = data

d = {'say': "Salut !", 'awnsers': [
                                  ["Comment vas tu ?",
                                  {'say': 'Bien et toi ?', 'answers': [
                                                                      ['Bien Merci']
                                                                      ]}],
                                  ["Vas te faire foutre !",
                                  {'say': 'Toi meme !', 'awnsers': [
                                                                   ['Connard']
                                                                   ]}]
                                  ]}

def parle(arg, rep):
    if arg[answers] == []:
        print(arg['say'])
    else:
        for i in arg['answers']:
            print(arg['answers'].index(i), i)
        parle(arg['answers'][rep][1])
