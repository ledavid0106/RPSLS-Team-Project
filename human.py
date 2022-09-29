
from player import Player


class Human(Player):
    def __init__(self, number):
        self.player_number = number
        self.name = self.name_player()
        super().__init__()
    
    def select_choice(self):
        pick = input(f"{self.name}, what would you like to choose? \n{self.options_names}\n")
        while pick not in self.options_names:
            pick = input(f"Please re-input your selection. \n{self.options_names}\n")
        for option in self.options:
            if pick == option.name:
                self.choice = option

    def name_player(self):
        result = input(f"Player {self.player_number}, what is your name? \n")
        print()
        return result

