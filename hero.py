from .character import Character

class Hero(Character):
    def attack(self):
       pass
    def defence(self):
       pass


class Warrior(Hero):
    # health_koef = 1
    defence_koef = 2
    attack_koef = 3



