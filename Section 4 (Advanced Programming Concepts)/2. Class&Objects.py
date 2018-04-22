

class Enemy:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("Atk: " ,self.atkl)

    def get_hp(self):
        print("HP: ", self.hp)


enemy1 = Enemy(600, 700)
enemy1.getAtk()
enemy1.get_hp()

enemy2 = Enemy(100, 220)
enemy2.getAtk()
enemy2.get_hp()
