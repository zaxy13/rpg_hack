import random

### start of Actor area ###

class Actor(object):
    """ the base class for all game characters """
    def __init__(self, name, x,y, room):
        self.name = name
        self.level = 1
        self.health = 50
        self.attack_points = 10
        self.defence_points = 10
        self.room = room
        self.pos = {"x":x,"y":y}

    def attack(self):
        return self.attack_points

    def attack_chance(self):
        luck = random.random()
        luck * 10.0
        if luck <= 80.0:
            return True
        else:
            return False

    def defence(self):
        return self.defence_points

    def defence_chance(self):
        luck = random.random()
        luck * 10.0
        if luck > 50.0:
            return True
        else:
            return False

    def hp(self, change, add=False):
        if add == True:
            self.health + change
        else:
            self.health - change

    def move(self, x, y):
        new_pos = {"x":x,"y":y}
        max_x = self.room.x
        max_y = self.room.y
        objects = self.room.objects

        if new_pos["x"] <= max_x and new_pos["y"] <= max_y:
            for obj in objects:
                if obj["pos"]["x"] == new_pos["x"] and obj["pos"]["y"] == new_pos["y"]:
                    print "there is an object there"
                    #todo build a look up for objects
                else:
                    self.pos = {"x":new_pos["x"],"y":new_pos["y"]}
        else:
            print "out of bounds"


class Player(Actor):
    def __init__(self, name, x, y, room):
        super(Player, self).__init__(name, x,y, room)
        self.gold = 100
        self.exp = 0
        self.next_level = 100
        # self.mana = 50
        # self.stamina = 50 to complex right now.
        self.weapon = {"attack":10, "chance":3, "name":"basic sword"}
        # todo, make an item class, to will make objects much neater.

    def Levelup(self):
        if self.exp >= self.next_level:
            self.level += 1
            self.exp = self.exp - self.next_level
            self.next_level = self.level ** self.level
            #todo make better exp growth
        else:
            print "you didn't level up"


class Enemy(Actor):
    def __init__(self, name, x,y, room):
        super(Enemy, self).__init__(name, x,y ,room)
        self.gold = 10
        self.loot = {}

    def exp_drop(self, player_level):
        return (self.level * 100) / player_level
        #todo better exp drops, maybe?

### end of Actor area ###
### Start of Room area ###

class Room(object):
    """ Base class for all types of spaces in game """
    def __init__(self, x, y ):
        self.x = x
        self.y = y
        self.objects = []

    def add_object(self, x, y, type, id):
        """ function to add objects to room, it's mostly to test things right now """
        new_obj = {"pos":{"x":x,"y":y}, "type":type, "r_obj_ID": id}

        for obj in self.objects:
            if x == obj["pos"]["x"] and y == obj["pos"]["y"]:
                return "that spot already full"
            else:
                self.objects.append(new_obj)
                print "object added"
        # if the list is empty, the for loop will nor run.
        self.objects.append(new_obj)
        print "first object in list"

### end of Room area ###
### start of actions ###

def action_attack(attacker, oppnet):
    """ Basic battler """
    hit_power = attacker.attack()
    hit_chance = attacker.attack_chance()
    defence_chance = oppnet.defence_chance()
    defence_power = oppnet.defence()


    if hit_chance == True:
        if defence_chance == True:
            hit_total = hit_power - defence_power
            if hit_total <= 0:
                hit_total = 0
            oppnet.hp(hit_total)
            if oppnet.health <= 0:
                return "oppnet dead"
            else:
                return "you hit with a force of %s hit points" % hit_total
        else:
            hit_total = hit_power
            if hit_total <= 0:
                hit_total = 0
            print oppnet.health
            oppnet.hp(hit_total)
            print oppnet.health
            if oppnet.health <= 0:
                return "oppnet dead"
            else:
                return "you hit with a full force of %s hit points" % hit_total
    else:
        return "ya missed...."


### end of actions ###


def main():
    pass


if __name__ == '__main__':
    main()
