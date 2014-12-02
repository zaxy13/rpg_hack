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
