import random
from player import Player


class AI(Player):
    def __init__(self):
        # self.names = ["John", "Joe", "Jack", "Joseph", "Jordan", "James", "Dan"]
        self.name = random.choice(["John", "Joe", "Jack", "Joseph", "Jordan", "James", "Dan"])
        super().__init__()
    
    