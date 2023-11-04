from .character import Character

class Enemy(Character):
    def atack(self):
        pass
    def defence(self):
        pass

class Zombi(Enemy):
    defence_koef = 1
    attack_koef = 4
class Skelet(Enemy):
    defence_koef = 2
    attack_koef = 3