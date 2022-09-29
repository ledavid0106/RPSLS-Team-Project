from gesture import Gesture

class Player:
    def __init__(self):
        self.options = [Gesture('Rock',['Scissors','Lizard'],['crushes','crushes']), 
        Gesture('Paper',['Rock','Spock'],['covers','disproves']), 
        Gesture("Scissors",['Paper','Lizard'],['cuts','dicapitates']), 
        Gesture('Lizard',['Paper','Spock'],['posions','eats']), 
        Gesture("Spock",['Scissors','Rock'],['smashes','vaporizes'])]
        self.choice = ""
        self.points = 0
        self.options_names = ['Rock','Paper','Scissors','Lizard','Spock']

