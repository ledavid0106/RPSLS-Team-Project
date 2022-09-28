
from AI import AI
from human import Human


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

    def determine_players(self):
        players = (input("How many players are playing?\n"))
        while True:
            if players.isnumeric() and int(players) in range(0,3):
                players = int(players)
                break
            else:
                players = input('Please reselect the number of players: 0, 1 or 2\n')
        
        if players == 2 :
            self.player1 = Human()
            self.player2 = Human()
        if players == 1:
            self.player1 = Human()
            self.player2 = AI()
        if players == 0 :
            self.player1 = AI()
            self.player2 = AI()

