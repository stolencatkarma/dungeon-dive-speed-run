from src.creature import Creature

class Player(Creature):
    def __init__(self):
        super().__init__()
        self.strength = 0
        self.speed = 0
        self.intelligence = 0
        self.resource = 0

        self.explored_tiles = dict() # level and locations of revealed tiles.

        # players can have two skills and one 'action' button for interacting with the world.
