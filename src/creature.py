class Creature:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hp = 0
        # each creature in game can have up to two skills.
        self.skill1 = None
        self.skill2 = None
        self.target = None

    def find_target(self):
        # if player is near make the player the target.
        pass

    def move(self, x, y):
        pass

    def use_skill(self, skill, x, y):
        pass

    def decide_next_action(self):
        pass

    def load(self, file):
        # load creature data from file
        pass
