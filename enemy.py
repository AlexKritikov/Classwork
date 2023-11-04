from .character import Character
import random

class Enemy(Character):
    def atack(self):
        pass
    def defence(self):
        pass
    def choose_action(self):
        enemy_act = random.randint(1,2)
        if enemy_act == 1:
            return 'Attack'
        else:
            return 'Defence'


class Zombi(Enemy):
    defence_koef = 1
    attack_koef = 4
class Skelet(Enemy):
    defence_koef = 2
    attack_koef = 3


