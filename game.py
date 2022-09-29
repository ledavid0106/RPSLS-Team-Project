
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
        print("           Welcome to Rock, Paper, Scissors, Lizard, Spock")
        print()
        # time.sleep(2)
    
    def rules(self):
        print("Each player selects an option from the given list.") 
        print("Each option will beat another option, lose against another option, or tie against the same option")
        print()
        print("               Here are the different outcomes")
        time.sleep(.5)
        print()
        print("                  Rock crushes Scissors")
        time.sleep(.5)
        print("                  Scissors cuts Paper")
        time.sleep(.5)
        print("                  Paper covers Rock")
        time.sleep(.5)
        print("                  Rock crushes Lizard")
        time.sleep(.5)
        print("                  Lizard poisons Spock")
        time.sleep(.5)
        print("                  Spock smashes Scissors")
        time.sleep(.5)
        print("                  Scissors decapitates Lizard")
        time.sleep(.5)
        print("                  Lizard eats Paper")
        time.sleep(.5)
        print("                  Paper disproves Spock")
        time.sleep(.5)
        print("                  Spock vaporizes Rock")
        time.sleep(.5)
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


    def player1_wins(self,phrase):
        print(f'{self.player1.name}\'s {self.player1.choice.name} {phrase} {self.player2.name}\'s {self.player2.choice.name}!')
        self.player1.points += 1
        print()

    def player2_wins(self,phrase):
        print(f'{self.player2.name}\'s {self.player2.choice.name} {phrase} {self.player1.name}\'s {self.player1.choice.name}!')
        self.player2.points += 1
        print()           


    def display_tally(self):
        print(f"{self.player1.name} has {self.player1.points} points || {self.player2.name} has {self.player2.points} points")
        print()
    
    def outcome(self):
        self.player1.select_choice()
        if self.humans == True:
            for count in range(50):
                print()
        self.player2.select_choice()
        print()
        if self.player1.choice.name == self.player2.choice.name:
            print(f'Both players picked {self.player1.choice.name} and neither player scored!')
            print()
        elif self.player2.choice.name in self.player1.choice.beats:
            if self.player2.choice.name == self.player1.choice.beats[0]:
                self.player1_wins(self.player1.choice.phrase[0])
            else:
                self.player1_wins(self.player1.choice.phrase[1])        
        else:
            if self.player1.choice.name == self.player2.choice.beats[0]:
                self.player1_wins(self.player2.choice.phrase[0])
            else:
                self.player1_wins(self.player2.choice.phrase[1])     
            

        if self.human:
            time.sleep(1.5)
        self.display_tally()
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