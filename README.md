Secret Project One
==================

The point of project one is to get back in to coding after I had spent some time
away. I want to work on a basic text based game in python.

Goals
-----
+ Have a robust game engine
+ A playable character
+ Enemies that drop loot and Exp
+ A level system, with an ability tree
+ NPCs that run shops and things
+ A Quest system
+ Dungeons and towns

Mechanics
---------
Here I will lay out the mechanics of the game, these differ from the
implementations as the mechanics are the systems that the code will aim for,
but not how it will achieve them. Think of it as a road map, expanding the
gaols and guiding the programmer.

### leveling
The game will feature a central level system that many of the other systems
get there base from, so it has to be pretty solid. <span
 style="color:red;">As of right now it is need of a lot of work.</span>

As in most games the level system is based on getting EXP points to advance
to the next level.
In this game after each level the level up cost will
increase exponentially to a level cap; what the level cap is and the curve it
will follow have yet to be set, as I plan to play test the game quite a bit.
After the level up goal is met the EXP counter will rest to zero, and any
points earned past the level up goal will roll over to the new counter.

EXP points can be earned in a few ways, killing opponents, completing quests,
and any other flanged event (such as finding rare loot, or completing
achievements).

### Stats
As stated prior, many of the games mechanics will be based on level, like
almost the stats. Things like health, attack, defense will have a direct tie
to the level of the Actor (As that is the base class it will effect all
  characters).

Implementations
---------------
Here I will lay out how I will make the basics parts of the game.

### Actor Class
This is the class that all the characters for the game will inherit from, NPCs,
Enemies, and the Player.

Base class:

    Actor():
        str name
        int level
        int health
        int attack_power
        int defence_power
        tupple position

Player class:

    Player():
      dict weapon
      dict armor
      int exp
      int gold
      int mana
      int stamina
      dict loot_sack

Enemy class:

    Enemy():
      dict loot
      int droped_gold
      str quest_flag

NPC class:

    npc():
      list_of_str dialog
      str job (my have other functions for some NPCs)
      str quest_flag


### Room Class
This is the class that all places in the game will inherit from, towns, dungeons,
homes, and shops.

Base class:

    Room():
      str name
      str description
      tupple x,y cords
      dict objects_in_room
