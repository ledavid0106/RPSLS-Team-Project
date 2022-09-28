from random import random
from player import Player


class AI(Player):
    def __init__(self):
        self.name = random.choice(["John", "Joe", "Jack", "Joseph", "Jordan", "James", "Dan"])
        super().__init__()

    def select_choice(self):
        self.choice = random.choice(self.options)
        