
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
        self.rules_list = ['Rock crushes Scissors','Scissors cuts Paper','Paper covers Rock',
        'Rock crushes Lizard','Lizard poisons Spock','Spock smashes Scissors', 'Scissors decapitates Lizard',
        'Lizard eats Paper', 'Paper disproves Spock','Spock vaporizes Rock']
        super().__init__()
    
    def intro(self):
        print('''                 
                                        Welcome to Rock, Paper, Scissors, Lizard, Spock 
        ''')
        time.sleep(1.65)
    
    def rules(self):
        print('''                                      Each player selects an option from the given list.
          
                Each option will beat another option, lose against another option, or tie against the same option
        
                                             Here are the different outcomes:
                                             ''')
        for rule in self.rules_list:
            print(f'                                                   {rule}')
            time.sleep(.25)
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
        elif players == 1:
            self.player1 = Human(1)
            self.player2 = AI()
            self.human = True
        elif players == 0 :
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

    def display_tally(self):
        print(f"{self.player1.name} has {self.player1.points} points || {self.player2.name} has {self.player2.points} points")
        print()
    
    def gameplay(self):
        while self.player1.points < self.points_win and self.player2.points < self.points_win:
            self.player1.select_choice()
            if self.humans == True:
                for count in range(50):
                    print()
            self.player2.select_choice()
            print()
            self.player1.score_point(self.player2)
            print()
            if self.human:
                time.sleep(1.5)
            self.display_tally()
            if self.human:
                time.sleep(1.5)

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