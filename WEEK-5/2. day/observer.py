class Warrior:
    def __init__(self):
        self.companions = []
        self.hp = 100

    def join(self,companion):
        self.companions.append(companion)

    def curse(self,opponet):
        opponet.join(Curse())
        self._notify_all('curse')

    def strike(self, opponet):
        opponet.inflict_damage(10)
        for companion in self.companions:
            companion.notify('strike',opponet)

    def inflict_damage(self,damage):
        self.hp -=damage
        self._notify_all('damage')

    def re_strike(self,damage):
        self.hp -= damage
        self._notify_all('re-strike')

    def heal(self,hp):
        self.hp += hp
        self._notify_all('heal')

    def _notify_all(self,type):
        for companion in self.companions:
            companion.notify(type,self)

class Healer:
    def notify(self,type,warrior):
        if type == 'damage':
            warrior.heal(10)

class Monster:
    def notify(self,type,opponent):
        if type == 'strike':
            opponent.re_strike(20)


class Curse:
    def notify(self,type,warrior):
        if type == 'damage':
            warrior.heal(-10)

class Cheer:
    def notify(self,type,warrior):
        if type == "curse":
            print('Hurry!')


class BattleField:
    def notify(self,type,warrior):
        print(type,' Somethioing happend!')

rabbit = Warrior()
wolf = Warrior()
fox = Monster()
shaman = Healer()
mouse = Cheer()

wolf.join(fox)
rabbit.join(shaman)
wolf.join(mouse)
rabbit.join(BattleField())
wolf.join(BattleField())


wolf.curse(rabbit)
wolf.strike(rabbit)
print(rabbit.hp)
print(wolf.hp)
