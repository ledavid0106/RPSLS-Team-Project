from gesture import Gesture

class Player:
    def __init__(self):
        self.name = self.name_player()
        self.options = [Gesture('Rock',['Scissors','Lizard'],['crushes','crushes']), 
        Gesture('Paper',['Rock','Spock'],['covers','disproves']), 
        Gesture("Scissors",['Paper','Lizard'],['cuts','dicapitates']), 
        Gesture('Lizard',['Paper','Spock'],['eats','posions']), 
        Gesture("Spock",['Scissors','Rock'],['smashes','vaporizes'])]
        self.choice = ""
        self.points = 0
        self.options_names = ['Rock','Paper','Scissors','Lizard','Spock']

    def name_player(self):
        return
    
    def select_choice(self):
        return 

    def score_point(self,player2):
        if self.choice.name == player2.choice.name:
            print(f'Both players picked {self.choice.name} and neither player scored!')
            print()
        elif player2.choice.name in self.choice.beats:
            if player2.choice.name == self.choice.beats[0]:
                print(f'{self.name}\'s {self.choice.name} {self.choice.phrase[0]} {player2.name}\'s {player2.choice.name}!')
                self.points += 1
            else:
                print(f'{self.name}\'s {self.choice.name} {self.choice.phrase[1]} {player2.name}\'s {player2.choice.name}!')
                self.points += 1                
        else:
            if self.choice.name == player2.choice.beats[0]:
                print(f'{player2.name}\'s {player2.choice.name} {player2.choice.phrase[0]} {self.name}\'s {self.choice.name}!')
                player2.points += 1
            else:
                print(f'{player2.name}\'s {player2.choice.name} {player2.choice.phrase[1]} {self.name}\'s {self.choice.name}!')
                player2.points += 1
                

    
