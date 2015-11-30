class Player:
    def __init__(self, name, HP = 100, damage = 10):
        self.name = name
        self.HP = HP
        self.damage = damage
        self.max_HP=100

    def print_status(self):
        if self.HP < 1:
            print(self.name + ' Dead')
        else:
            print(self.name + ' : ' + str(self.HP) )

    def strike(self,other):
        if other.HP < self.damage:
            other.HP = 0
        else:
            other.HP -= self.damage
        other.print_status()

    def drink_potion(self):
        self.HP += 10
        if self.HP > self.max_HP:
            self.HP = self.max_HP
        self.print_status()

class Cerlic(Player):
    def heal(self, ally):
        ally.HP += 10


Gyuri = Player('Gyuri',100,25)
Tahó = Player('Tahó',100,10)
Balázs = Cerlic('Balázs',100,20)

Gyuri.strike(Tahó)
for i in range (3):
    Gyuri.strike(Tahó)
    Balázs.heal(Tahó)

Tahó.print_status()
