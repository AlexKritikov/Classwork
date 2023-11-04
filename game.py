class Game:

    # init game
    def __init__(self):
        pass
        # init Hero
        # init Enemy
        # self.hero = todo
        # self.enemy = todo


    def choose_characters_action(self):
        hero_action = self.hero.choose_action()
        enemy_action = self.enemy.choose_action()
        return hero_action, enemy_action

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







    # battle

        # choose character

        # choose enemy

        # round -> repeat

        # battle result

    # ?