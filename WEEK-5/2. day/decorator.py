class Sword:
    def damage(self):
        return 10

class MagicWand:
    def damage(self):
        return 50

class Enhanced:
    def __init__(self,weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() + 5

class Magical:
    def __init__(self,weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() * 2


class Warrior:
    def __init__(self,weapon = Sword() ):
        self.hp = 100
        self.weapon = weapon

    def strike(self,opponent):
        damage = self.weapon.damage()
        opponent.hp -= damage

class Rusty:
    def __init__(self,weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() / 2

warrior = Warrior(Magical(Enhanced(Sword())))
warrior2 = Warrior(Magical(Enhanced(MagicWand())))
opponent = Warrior(Sword())
warrior.strike(opponent)
warrior2.strike(warrior)
print(warrior2.hp)
print(warrior.hp)
print(opponent.hp)
