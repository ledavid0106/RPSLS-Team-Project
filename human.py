
from player import Player


class Human(Player):
    def __init__(self, number):
        self.player_number = number
        self.name = self.name_space()
        super().__init__()
    
    def select_choice(self):
        self.choice = input(f"{self.name}, what would you like to choose? \n{self.options}\n")
        while self.choice not in self.options:
            self.choice = input(f"Please re-input your selection. \n{self.options}\n")

    def name_space(self):
        result = input(f"Player {self.player_number}, what is your name? \n")
        print()
        return result

