
from AI import AI
from human import Human


class Game:
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.humans = False
        super().__init__()
    
    def intro(self):
        print()
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock")
        print()
    
    def rules(self):
        print("Each player selects an option from the given list. Each option will beat another option, lose against another option, or tie against the same option")
        print("Here are the different outcomes")
        print("Rock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock")
        print()
        
    def determine_players(self):
        players = (input("How many players are playing?\n"))
        print()
        while True:
            if players.isnumeric() and int(players) in range(0,3):
                players = int(players)
                break
            else:
                players = input('Please reselect the number of players: 0, 1 or 2\n')
                print()
        if players == 2 :
            self.player1 = Human()
            self.player2 = Human()
            self.humans = True
        if players == 1:
            self.player1 = Human()
            self.player2 = AI()
        if players == 0 :
            self.player1 = AI()
            self.player2 = AI()

    def player1_wins(self):
        print(f'{self.player1.name}\'s {self.player1.choice} beats {self.player2.name}\'s {self.player2.choice}!')
        self.player1.points += 1
        print()

    def player2_wins(self):
        print(f'{self.player2.name}\'s {self.player2.choice} beats {self.player1.name}\'s {self.player1.choice}!')
        self.player2.points += 1
        print()           


    def rock_outcome(self):
        if self.player2.choice == 'Scissors':
            self.player1_wins()
            return
        if self.player2.choice == 'Paper':
            self.player2_wins()
            return
        if self.player2.choice == 'Lizard':
            self.player1_wins()
            return
        if self.player2.choice == 'Spock':
            self.player2_wins()
            return

    def paper_outcome(self):
        if self.player2.choice == 'Scissors':
            self.player2_wins()
            return
        if self.player2.choice == 'Rock':
            self.player1_wins()   
            return
        if self.player2.choice == 'Lizard':
            self.player2_wins()
            return
        if self.player2.choice == 'Spock':
            self.player1_wins()
            return    

    def scissors_outcome(self):
        if self.player2.choice == 'Paper':           
            self.player1_wins()
            return
        if self.player2.choice == 'Rock':
            self.player2_wins()   
            return
        if self.player2.choice == 'Lizard':
            self.player1_wins()
            return
        if self.player2.choice == 'Spock':
            self.player2_wins()
            return         

    def lizard_outcome(self):
        if self.player2.choice == 'Scissors':           
            self.player2_wins()
            return
        if self.player2.choice == 'Rock':
            self.player2_wins()  
            return
        if self.player2.choice == 'Paper':
            self.player1_wins()
            return
        if self.player2.choice == 'Spock':
            self.player1_wins()
            return

    def spock_outcome(self):
        if self.player2.choice == 'Scissors':           
            self.player1_wins()
            return
        if self.player2.choice == 'Rock':
            self.player1_wins()   
            return
        if self.player2.choice == 'Lizard':
            self.player1_wins()
            return
        if self.player2.choice == 'Paper':
            self.player2_wins()
            return              

    
    def outcome(self):
        self.player1.select_choice()
        if self.humans == True:
            for count in range(8):
                print()
        self.player2.select_choice()
        print()
        if self.player1.choice == self.player2.choice:
            print(f'Both players picked {self.player1.choice} and neither player scored!')
            print()
            return
        if self.player1.choice == 'Rock':
            self.rock_outcome()
        if self.player1.choice == 'Paper':
            self.paper_outcome()
        if self.player1.choice == 'Scissors':
            self.scissors_outcome()
        if self.player1.choice == 'Lizard':
            self.lizard_outcome()
        if self.player1.choice == 'Spock':
            self.spock_outcome()

    def gameplay(self):
        while self.player1.points < 2 and self.player2.points < 2:
            self.outcome()

    def display_winner(self):
        if self.player1.points == 2:
            print(f'{self.player1.name} is the Winner!')
        else:
            print(f'{self.player2.name} is the Winner!')

    def run_game(self):
        self.intro()
        self.rules()
        self.determine_players()
        self.gameplay()
        self.display_winner()