class Character:
    initial_health = 100
    initial_defence = 10
    initial_attack = 10

    health_koef = 1
    defence_koef = 1
    attack_koef = 1

    def __init__(self, name):
        self.name = name
        self.health_value = self.initial_health * self.health_koef
        self.defence_value = self.initial_defence * self.defence_koef
        self.attack_value = self.initial_attack * self.attack_koef

    def damage(self, value):
        print(f'{self.name} will get damage {value}. Health was:'
              f' {self.health_value}')

        self.health_value = self.health_value - value

        print(f'{self.name} got damage {value}. Health left: {self.health_value}')

    def is_alive(self):
        if self.health_value > 0:
            return True
        else:
            return False

