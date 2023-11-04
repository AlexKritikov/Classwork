from .character import Character
import random


    def attack(self):
       pass
    def defence(self):
       pass
class Enemy(Character):
    def atack(self):
        pass
    def defence(self):
        pass
enemy_act = random.randint(1,2)
class Zombi(Enemy):
    defence_koef = 1
    attack_koef = 4
class Skelet(Enemy):
    defence_koef = 2
    attack_koef = 3

def enemy_action():
    if enemy_act==1:
        Enemy.atack()
    else:
        Enemy.defence()
