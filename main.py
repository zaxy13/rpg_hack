import random
from Game_libs.Actors import Player, Enemy, NPC
from Game_libs.Rooms import Room

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




def main():
    r = Room(10,10)
    p = Player("bob", 2,2 ,r)
    e = Enemy("Troll") 3,3, r)
    print "ready"


if __name__ == '__main__':
    main()
