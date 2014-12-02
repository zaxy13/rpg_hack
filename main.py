### start of Actor area ###

class Actor(object):
    """ the base class for all game characters """
    def __init__(self, name, x,y):
        self.name = name
        self.level = 1
        self.health = 50
        self.attack = 10
        self.defence = 10
        self.pos = {"x":x,"y":y}

    def move(self, x, y, room):
        new_pos = {"x":x,"y":y}
        max_x = room.x
        max_y = room.y
        objects = room.objects

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
    def __init__(self, name, x,y):
        super(Player, self).__init__(name, x,y)
        self.gold = 100
        self.exp = 0
        self.next_level = 100
        self.mana = 50
        self.stamina = 50
        self.weapon = {"attack":10, "chance":3, "name":"basic sword"}

    def Levelup(self):
        if self.exp >= self.next_level:
            self.level += 1
            self.exp = self.exp - self.next_level
            self.next_level = self.level ** self.level
            #todo make better exp growth
        else:
            print "you didn't level up"

    def battle(self, opponent):
        pass

class Enemy(Actor):
    def __init__(self, name, x,y):
        super(Enemy, self).__init__(name, x,y)
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
        self.objects.append(new_obj)
        print "first object in list"

### end of Room area ###
def main():
    pass


if __name__ == '__main__':
    main()
