
from player import Player


class Human(Player):
    def __init__(self):
        self.name = input("What is your name? \n")
        super().__init__()
    
    def select_choice(self):
        self.choice = input(f"{self.name} What would you like to choose? \n{self.options}\n")


