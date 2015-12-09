class Weapon:
    def strike(self,warrior,opponet):
        opponet.hp -= self.damage()
        warrior.hp -= self.self_damage()

    def damage(self,type):
        return type.damage()

    def self_damage(self,type):
        return type.damage()

class Sword(Weapon):
    def damage(self):
        return 10

    def self_damage(self):
        return 1

class MagicWand(Weapon):
    def damage(self):
        return 20

    def self_damage(self):
        return 0

class None_weapon(Weapon):
    def damage(self):
        return 0

    def self_damage(self):
        return 0

class Enhanced(Weapon):
    def __init__(self,weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() * 2

    def self_damage(self):
        return self.weapon.damage() / 2




class Warrior:
    def __init__(self,weapon = None_weapon):
        self.hp = 100
        self.weapon = weapon

    def strike(self,opponet):
        self.weapon.strike(self,opponet)

    def __repr__(self):
        return "Warrior hp={}".format(self.hp)

warrior = Warrior(Sword())
palika = Warrior(MagicWand())
warrior.strike(palika)
print(warrior,'   ' ,palika)

palika.strike(warrior)
print(palika, '   ' ,warrior)

print('_________________________________')
warrior = Warrior(Enhanced(Sword()))
palika = Warrior(Enhanced(MagicWand()))
warrior.strike(palika)
print(warrior,'   ' ,palika)

palika.strike(warrior)
print(palika, '   ' ,warrior)
