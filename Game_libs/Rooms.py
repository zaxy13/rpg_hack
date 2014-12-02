
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
