class Skill:
    def __init__(self):
        self.name = 'unnamed'
        self.cooldown = 0
        self.group = 'movement' # melee_damage, ranged_damage
        self.range = 0 # how far away can we use this skill?
        self.targets = 0 # how many targets can we hit with this skill. can be the same more then once.
        self.damage = 0 # how much damage this skill does. if any.
