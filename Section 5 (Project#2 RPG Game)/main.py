from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Magic
fire = Spell("Fire", 10, 600, "black")
thunder = Spell("Thunder", 10, 600, "black")
blizzard = Spell("Blizzard", 10, 600, "black")
meteor = Spell("Meteor", 20, 1200, "black")
quake = Spell("Quake", 14, 500, "black")
cure = Spell("Cure", 12, 620, "white")
cura = Spell("Cura", 18, 1500, "white")

# Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party", 9999)
hielixir = Item("Hi-Elixir", "elixir", "Fully restores HP/MP of party", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# Player Items
player_items = [
        {"item": potion, "quantity": 5},
        {"item": hipotion, "quantity": 15},
        {"item": elixir, "quantity": 2},
        {"item": hielixir, "quantity": 1},
        {"item": grenade, "quantity": 2}]
# player Magics
player_magic = [fire, thunder, meteor, cure, cura]

# Instantiate Players
player1 = Person("Muiz ", 66, 152, 60, 34, player_magic, player_items, "alive")
player2 = Person("Valos", 4156, 144, 60, 34, player_magic, player_items, "alive")
player3 = Person("Semes", 5822, 174, 60, 34, player_magic, player_items, "alive")

# player list
players = [player1, player2, player3]

# Enemy Magics
enemy_magic = [fire, thunder, meteor]

# Instantiate Enemies
enemy1 = Person("Imp  ", 100, 130, 560, 325, enemy_magic, [], "alive")
enemy2 = Person("Magus", 18222, 701, 525, 25, enemy_magic, [], "alive")
enemy3 = Person("Imp  ", 1200, 130, 560, 325, enemy_magic, [], "alive")

# Enemy list
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "ENEMY ATTACKS!!!" + bcolors.ENDC)

defeated_player = 0
defeated_enemy = 0
while running:
    print("======================")
    print("\n")
    print("---------P-L-A-Y-E-R-S--------")
    for player in players:
        player.player_stats()
    print("---------E-N-E-M-I-E-S--------")
    for enemy in enemies:
        enemy.player_stats()
    print("--------------------------")

    p = 0
    for player in players:

        if players[p].status is "alive":
            player.choose_action()
            choice = input("Choose action: ")
            index =  int(choice) - 1
            enemy = player.choose_target(enemies)
            while enemies[enemy].status is "dead":
                print(enemies[enemy].name + " is already dead.")
                enemy = player.choose_target(enemies)

            if index is 0:
                dmg = player.generate_damage()
                enemies[enemy].take_damage(dmg)
                if enemies[enemy].hp == 0:
                    enemies[enemy].status = "dead"
                    print("\n" + bcolors.BOLD + bcolors.BOLD + enemies[enemy].name + " is dead!" + bcolors.ENDC)
                print(bcolors.BOLD + player.name + bcolors.ENDC + " attacked " + enemies[enemy].name + " for", dmg, "points of damage.")
            elif index is 1:
                player.choose_magic()
                magic_choice = int(input("Choose magic:")) - 1

                if magic_choice is -1:
                    continue

                spell = player.magic[magic_choice]
                magic_dmg = spell.generate_damage()

                current_mp = player.get_mp()
                if spell.cost > current_mp:
                    print(bcolors.FAIL+ "\nNot Enough Magic Points\n"+ bcolors.ENDC)
                    continue

                player.reduce_mp(spell.cost)
                if spell.type is "white":
                    player.heal(magic_dmg)
                    print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP."+ bcolors.ENDC)
                elif spell.type is "black":
                    enemies[enemy].take_damage(magic_dmg)
                    if enemies[enemy].hp == 0:
                        enemies[enemy].status = "dead"
                        print("\n" + bcolors.BOLD + bcolors.BOLD + enemies[enemy].name + " is dead!" + bcolors.ENDC)
                    print(bcolors.OKBLUE+"\n" +spell.name+ " deals", str(magic_dmg), "points of damage to " + enemies[enemy].name +bcolors.ENDC)

            elif index is 2:
                player.choose_items()
                item_choice = int(input("Choose item:")) - 1

                if item_choice is -1:
                    continue

                item = player.items[item_choice]["item"]

                if player.items[item_choice]["quantity"] is 0:
                    print(bcolors.FAIL + "\nYou have no "+ item.name + bcolors.ENDC)
                    continue
                else:
                    player.items[item_choice]["quantity"] -= 1

                if item.type is "potion":
                    player.heal(item.prop)
                    print(bcolors.OKGREEN + "\n" + item.name + " heals you for", item.prop, "HP" +bcolors.ENDC)

                elif item.type is "elixir":
                    if item.name == "hielixir":
                        for i in players:
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.OKGREEN+ "\n" + item.name + " fully restores all your peer's HP/MP" + bcolors.ENDC)

                elif item.type is "attack":
                    enemies[enemy].take_damage(item.prop)
                    if enemies[enemy].hp == 0:
                        enemies[enemy].status = "dead"
                        print("\n" + bcolors.BOLD + bcolors.BOLD + enemies[enemy].name + " is dead!" + bcolors.ENDC)
                    print(bcolors.FAIL + "\n"+ item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy].name + bcolors.ENDC)
        p += 1

    print(bcolors.FAIL + bcolors.BOLD + "ENEMY ATTACKS!!!" + bcolors.ENDC)
    enemy = 0
    for i in enemies:
        if enemies[enemy].status is "alive":
            enemy_choice = random.randrange(0, 2)
            target = random.randrange(0, len(players)-1)
            while players[target].status != "alive":
                target = random.randrange(0, len(players) - 1)

            if enemy_choice is 0:
                enemy_dmg = enemies[enemy].generate_damage()
                players[target].take_damage(enemy_dmg)
                print("\n" + enemies[enemy].name +" attacks " + bcolors.BOLD + players[target].name + bcolors.ENDC + " for", enemy_dmg, "points of damage.")

            elif enemy_choice is 1:
                magic_choice = random.randrange(0, len(enemy_magic))
                spell = enemies[enemy].magic[magic_choice]
                magic_dmg = spell.generate_damage()

                current_mp = enemies[enemy].get_mp()
                while spell.cost > current_mp:
                    current_mp = enemies[enemy].get_mp()

                enemies[enemy].reduce_mp(spell.cost)
                players[target].take_damage(magic_dmg)
                if players[target].hp == 0:
                    players[target].status = "dead"
                    print("\n" + bcolors.BOLD + players[target].name + " is dead!" + bcolors.ENDC)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg),
                      "points of damage to " + players[target].name + bcolors.ENDC)

            if players[target].get_hp() == 0:
                players[target].status = "dead"
                defeated_player += 1
                print("\n"+bcolors.BOLD + bcolors.FAIL + players[target].name + " is dead!"+ bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                enemies[enemy].status = "dead"
                defeated_enemy += 1
                print("\n" + bcolors.BOLD + bcolors.FAIL + enemies[enemy].name + " is dead!" + bcolors.ENDC)

        if defeated_enemy >= 2:
            print(bcolors.OKGREEN + "Players Win!" + bcolors.ENDC)
            running = False
            break
        elif defeated_player >=2:
            print(bcolors.FAIL + "Players Lost!! Enemy has defeated players" + bcolors.ENDC)
            running = False
            break
        enemy += 1
