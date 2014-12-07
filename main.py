
from Game_libs.Actors import Player, Enemy, NPC
# I'm going a different direction for now
# from Game_libs.Rooms import Room


# test entities
p = Player("bob")
e = Enemy("troll")


def battler(attacker, defender):
    """ Basic battler """
    hit_power = attacker.attack()
    hit_chance = attacker.attack_chance()
    defence_chance = defender.defence_chance()
    defence_power = defender.defence()

    # todo, change the strings that are returned for code/ids so that the mechanics engine can deal with the print out
    if attacker.health != 0 and defender.health != 0:
        if hit_chance:
            if defence_chance:
                hit_total = hit_power - defence_power
                if hit_total <= 0:
                    hit_total = 0
                defender.hp(hit_total)
                if defender.health <= 0:
                    return "defender dead"
                else:
                    return "{} blocked, you hit with a force of {} hit points".format(defender.name, hit_total)
            else:
                hit_total = hit_power
                if hit_total <= 0:
                    hit_total = 0
                if defender.health <= 0:
                    return "defender dead"
                else:
                    return "{} was wide open, you hit with full force, {} hit points".format(defender.name, hit_total)
        else:
            return "ya missed...."
    elif attacker.health <= 0:
        return "Can't Attack, Your dead"
    elif defender.health <= 0:
        return "Can't Attack, {} is dead".format(defender.name)

def main():
    p = Player("bob")
    e = Enemy("Troll")
    battler(p, e)
    print("done")


if __name__ == '__main__':
    main()
