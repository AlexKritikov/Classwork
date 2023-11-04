from .hero import Warrior, Charmer
from .enemy import Skelet, Zombi


class Game:
    def __init__(self):
        pass
        # init Hero
        self.hero = self.init_hero()

        # init Enemy
        self.enemy = self.init_enemy()

    def init_hero(self):
        user_choice = input("W if warrior or C if Charmer")
        if user_choice == "W":
            return Warrior("Warrior")
        else:
            return Charmer("Charmer")


    def choose_characters_action(self):
        hero_action = self.hero.choose_action()
        enemy_action = self.enemy.choose_action()
        return hero_action, enemy_action

    def init_enemy(self):
        # Alexander
        pass

    def hero_attack(self, enemy_action):
        attack_value = self.hero.attack_value

        if enemy_action == 'Defence':
            attack_value -= self.enemy.defence_value

        if attack_value > 0:
            self.enemy.damage(attack_value)

    def enemy_attack(self, hero_action):
        attack_value = self.enemy.attack_value

        if hero_action == 'Defence':
            attack_value -= self.enemy.defence_value

        if attack_value > 0:
            self.hero.damage(attack_value)


    def battle(self):
        print('Start a new round')

        # choose action
        hero_action, enemy_action = self.choose_characters_action()

        if hero_action == 'Defence' and enemy_action == 'Defence':
            print('Both choose "Defence". No damage')
            self.battle()

        # todo: use random here
        if hero_action == 'Attack':
            self.hero_attack(enemy_action)

        if self.enemy.is_alive(self):
            if enemy_action == 'Attack':
                self.enemy_attack(hero_action)

        if self.enemy.is_alive() and self.hero.is_alive():
            self.battle()
        elif self.enemy.is_alive() == False:
            print(f'Hero {self.hero.name} win!')
        else:
            print(f'Enemy {self.enemy.name} win!')
