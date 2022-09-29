
from AI import AI
from human import Human
import time

class Game:
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.humans = False
        self.human = False
        self.points_win = 0
        
        super().__init__()
    
    def intro(self):
        print()
        print("                  Welcome to Rock, Paper, Scissors, Lizard, Spock")
        print()
        time.sleep(2.5)
    
    def rules(self):
        print("                  Each player selects an option from the given list.") 
        print("                  Each option will beat another option, lose against another option, or tie against the same option")
        print()
        print("                  Here are the different outcomes")
        time.sleep(1)
        print()
        print("                  Rock crushes Scissors")
        time.sleep(1)
        print("                  Scissors cuts Paper")
        time.sleep(1)
        print("                  Paper covers Rock")
        time.sleep(1)
        print("                  Rock crushes Lizard")
        time.sleep(1)
        print("                  Lizard poisons Spock")
        time.sleep(1)
        print("                  Spock smashes Scissors")
        time.sleep(1)
        print("                  Scissors decapitates Lizard")
        time.sleep(1)
        print("                  Lizard eats Paper")
        time.sleep(1)
        print("                  Paper disproves Spock")
        time.sleep(1)
        print("                  Spock vaporizes Rock")
        time.sleep(1)
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
            self.player1 = Human(1)
            self.player2 = Human(2)
            self.humans = True
            self.human = True
        if players == 1:
            self.player1 = Human(1)
            self.player2 = AI()
            self.human = True
        if players == 0 :
            self.player1 = AI()
            self.player2 = AI()

    def point_to_win(self):
        self.points_win = (input("How many points do you want required to win?\n"))

        while True:
            if self.points_win.isnumeric():
                self.points_win = int(self.points_win)
                break
            else:
                self.points_win = input('Please enter a valid number.\n')
                print()
        print()


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
            self.player2_wins()
            return
        if self.player2.choice == 'Paper':
            self.player2_wins()
            return              

    def tally(self):
        print(f"{self.player1.name} has {self.player1.points} points || {self.player2.name} has {self.player2.points} points")
        print()
    
    def outcome(self):
        self.player1.select_choice()
        if self.humans == True:
            for count in range(50):
                print()
        self.player2.select_choice()
        print()
        if self.player1.choice == self.player2.choice:
            print(f'Both players picked {self.player1.choice} and neither player scored!')
            print()
        if self.player1.choice == 'Rock':
            self.rock_outcome()
        elif self.player1.choice == 'Paper':
            self.paper_outcome()
        elif self.player1.choice == 'Scissors':
            self.scissors_outcome()
        elif self.player1.choice == 'Lizard':
            self.lizard_outcome()
        elif self.player1.choice == 'Spock':
            self.spock_outcome()
        if self.human:
            time.sleep(1.5)
        self.tally()
        if self.human:
            time.sleep(1.5)


    def gameplay(self):
        while self.player1.points < self.points_win and self.player2.points < self.points_win:
            self.outcome()

    def display_winner(self):
        if self.player1.points == self.points_win:
            print(f'{self.player1.name} is the Winner!')
        else:
            print(f'{self.player2.name} is the Winner!')

    def run_game(self):
        self.intro()
        self.rules()
        self.determine_players()
        self.point_to_win()
        self.gameplay()
        self.display_winner()