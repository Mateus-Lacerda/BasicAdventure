import random


class boss:
    
    def __init__(self, name, attack_type):
        self.name = name
        self.attack_type = attack_type

    life = random.randint(30,50)
    strength = random.randint(10,15)
    