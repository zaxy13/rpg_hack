### start of Actor area ###
import random

class Actor(object):

    """ the base class for all game characters """

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 50
        self.attack_points = 10
        self.defence_points = 10

    # return the base attack points, ment to be overridden in Player subclass
    def attack(self):
        return self.attack_points

    # look in to changing both chances to just luck, then in Player subclass add bonuses.
    def attack_chance(self):
        luck = random.random() * 100.0
        print("luck_atk", luck)
        if luck <= 80.0:
            return True
        else:
            return False

    def defence(self):
        return self.defence_points

    def defence_chance(self):
        luck = random.random() * 100.0
        # print("luck_def", luck)
        if luck > 50.0:
            return True
        else:
            return False

    def hp(self, change, add=False):

        if add:
            self.health += change
        else:
            self.health -= change


class Player(Actor):
    def __init__(self, name):
        super(Player, self).__init__(name)
        self.gold = 100
        self.exp = 0
        self.next_level = 100
        self.weapon = {"attack": 10, "chance": 3, "name": "basic sword"}
        # todo, make an item class, to will make objects much neater.

    def level_up(self):
        if self.exp >= self.next_level:
            self.level += 1
            xp = self.exp - self.next_level
            self.exp = xp
            self.next_level = self.level ** self.level
            # todo make better exp growth
        else:
            print("you didn't level up")


class Enemy(Actor):
    def __init__(self, name):
        super(Enemy, self).__init__(name)
        self.gold = 10
        self.loot = {}

    def exp_drop(self, player_level):
        return (self.level * 100) / player_level
        # todo better exp drops, maybe?


class NPC(Actor):
    pass
### end of Actor area ###
