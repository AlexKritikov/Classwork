from character import Character

class Hero(Character):
    def choose_action(self):
        result = input("Enter your Action A = Attack or B = Defense")
        if result == "A":
            return "Attack"
        else:
            return "Defense"

class Warrior(Hero):
    defence_koef = 2
    attack_koef = 3


class Charmer(Hero):
    defence_koef = 3
    attack_koef = 2
