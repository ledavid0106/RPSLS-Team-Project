import random
from player import Player


class AI(Player):
    def __init__(self):
        self.name = random.choice(["Darth Vader", "Ursala", "Jack-the-Ripper", "Maleficient", "Hans Gruber", "Khan", "Cpt. Hook"])
        super().__init__()

    def select_choice(self):
        self.choice = random.choice(self.options)
        
