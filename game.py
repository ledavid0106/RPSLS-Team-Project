
class Game:
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        super().__init__()
    
    def intro(self):
        print()
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock")
        print()
    
    def rules(self):
        print("Each player selects an option from the given list. Each option will beat another option, lose against another option, or tie against the same option")
        print("Here are the different outcomes")
        print("Rock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock")



