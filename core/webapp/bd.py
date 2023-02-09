from random import random, randint


class DataBase:
    name = None
    age = randint(1, 12)
    satiety = 20
    happiness = 20
    energy = 20

    @classmethod
    def play(cls):
        if random() < 0.3:
            cls.happiness = 0
        else:
            cls.happiness += 15
            cls.satiety -= 10

    @classmethod
    def eat(cls):
        if cls.satiety >= 100:
            pass
        else:
            cls.satiety += 15
            cls.happiness += 5

    @classmethod
    def sleep(cls):
        cls.energy += 15

    @classmethod
    def action(cls, action):
        if action:
            if action == 'play':
                cls.play()
            elif action == 'eat':
                cls.eat()
            else:
                cls.sleep()
