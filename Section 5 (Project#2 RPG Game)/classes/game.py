import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items, status):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic", "Items"]
        self.items = items
        self.name = name
        self.status = status

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def take_damage(self,dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n------ "+ bcolors.BOLD + self.name +":\n  # Actions: ")
        for item in self.actions:
            print("       " +str(i)+ ":", item)
            i+=1

    def choose_magic(self):
        i = 1
        print("\n  # Magic: ")
        for spell in self.magic:
            print("       " +str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_items(self):
        i = 1
        print("\n   # Items: ")
        for item in self.items:
            print("       " + str(i) + ":", item["item"].name, "(" + item["item"].description + ") x" + str(item["quantity"]))
            i += 1

    def choose_target(self, enemies):
        i = 1;
        print("Enemies in front: 1-", len(enemies))
        for enemy in enemies:
            if enemy.status == "alive":
                print("       " + str(i) + ":"+ enemy.name )
            else:
                print("       " + bcolors.FAIL +str(i) + ":"+ enemy.name + bcolors.ENDC )
            i += 1

        choice =  int(input("       Choose a Target: ")) - 1
        return choice

    def player_stats(self):
        HP_bar = ""
        HP_bar_ticks = (self.hp/self.maxhp) * 100 /4
        while HP_bar_ticks > 0:
            HP_bar += "█"
            HP_bar_ticks -= 1


        while len(HP_bar) < 25:
            HP_bar += " "

        MP_bar = ""
        MP_bar_ticks = (self.mp / self.maxmp) * 100 / 10
        while MP_bar_ticks > 0:
            MP_bar += "█"
            MP_bar_ticks -= 1

        while len(MP_bar) < 10:
            MP_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            Decreased = 9 - len(hp_string)

            while Decreased > 0:
                current_hp +=  " "
                Decreased -=1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 9 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1

                current_mp += mp_string
        else:
            current_mp = mp_string

        print(bcolors.BOLD + self.name + ":     " + current_hp + "|" + bcolors.OKGREEN + HP_bar
              + bcolors.ENDC+ "| HP\n             " + bcolors.BOLD + current_mp
              + "|" + bcolors.OKBLUE + MP_bar + bcolors.ENDC + "| MP")

