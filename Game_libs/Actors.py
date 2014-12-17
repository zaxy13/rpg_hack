### start of Actor area ###
import random


class Actor(object):

    """ the base class for all game characters """

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.health = 50
        self.attack_points = 10
        self.defence_points = 10

    # return the base attack points, ment to be overridden in Player subclass
    def attack(self):
        return self.attack_points

    # look in to changing both chances to just luck, then in Player subclass add bonuses.
    def attack_chance(self):
        luck = random.random() * 100.0
        if luck <= 80.0:
            return True
        else:
            return False

    def defence(self):
        return self.defence_points

    def defence_chance(self):
        luck = random.random() * 100.0
        if luck > 50.0:
            return True
        else:
            return False

    def hp(self, change, add=False):
        if add:
            self.health += change
        else:
            self.health -= change

    def exp_drop(self):
        return self.level * 100
        # todo better exp drops, maybe?

    def level_up(self, exp_gain ):
        pass

    def equip_item(self, item=None):
        pass


class Player(Actor):
    def __init__(self, name):
        super(Player, self).__init__(name)
        self.gold = 100
        self.next_level = 100
        self.weapon = None
        self.armor = None
        # todo, make an item class, to will make objects much neater.

    # todo add auto check ability

    def level_up(self, exp_gain):
        self.exp = self.exp + exp_gain

        if self.exp >= self.next_level:
            self.level += 1
            xp = self.exp - self.next_level
            self.exp = xp
            self.next_level = 50*self.level**2+50*self.level
            print("yay, you leveled up!")
            # todo make better exp growth
        else:
            print("you didn't level up")

    def equip_item(self, itemm, kind="pack"):
        if kind != "pack":
            if kind == "weapon":
                self.weapon = itemm
            elif kind == "armor":
                self.armor = itemm

        else:
            return "item add fail"





class Enemy(Actor):
    def __init__(self, name):
        super(Enemy, self).__init__(name)
        self.gold = 10
        self.loot = {}




class NPC(Actor):
    pass

def emaker(names):
    e = {}
    x = 0
    for name in names:
        e["e{}".format(x)] = Enemy(name)
        x += 1
    return e
