__author__ = 'Zaxy'


class Item(object):
    """ Base class for all items in the game """
    def __init__(self, name, description, durability, kind):
        self.name = name
        self.description = description
        self.durability = durability
        self.kind = kind

    def get_item(self):
        item = {"name": self.name, "description": self.description}
        return item

    def damage(self, amount=1):
        if self.durability > 0:
            self.durability -= amount
        else:
            return "{} is broken".format(self.name)


class Weapon(Item):

    def __init__(self, name, description, hit_bonus=0, hit_chance=0, durability=100, stat_effect=None, element_effect=None):
        kind = "Weapon"
        super(Weapon, self).__init__(name, description, durability, kind)
        self.hit_bonus = hit_bonus
        self.hit_chance = hit_chance
        self.stat_effect = stat_effect
        self.element_effect = element_effect

    def get_item(self):
        item = {"name": self.name, "description": self.description, "durability": self.durability,
                "hit_bonus": self.hit_bonus, "hit_chance": self.hit_chance,
                "stat_effect": self.stat_effect, "element_effect": self.element_effect}
        return item


class Armor(Item):

    def __init__(self, name, description, defence_bonus=0, defence_chance=0, stat_effect=None, element_effect=None):
        kind = "Armor"
        super(Armor, self).__init__(name, description, kind)
        self.defence_bonus = defence_bonus
        self.defence_chance = defence_chance
        self.stat_effect = stat_effect
        self.element_effect = element_effect

    def get_item(self):
        item = {"name": self.name, "description": self.description, "durability": self.durability,
                "defence_bonus": self.defence_bonus, "defence_chance": self.defence_chance,
                "stat_effect": self.stat_effect, "element_effect": self.element_effect}
        return item















