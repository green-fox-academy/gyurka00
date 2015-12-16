import random
class Character():
    def __init__(self, name = ''):
        self.name = name
        self.random_stats()

    def random_stats(self):
        self.dexterity = self.roll() + 6
        self.health = self.roll() + self.roll() + 12
        self.max_dexterity = self.dexterity
        self.max_health = self.health

    @staticmethod
    def roll():
        number = random.randrange(1, 6)
        return number

    def print_stats(self):
        output = ''
        output += 'Max Dexterity: ' + str(self.max_dexterity) + '\n'
        output += 'Current Dexterity: ' + str(self.dexterity) + '\n'
        output += 'Max Health: ' + str(self.max_health) + '\n'
        output += 'Current Health: ' + str(self.health) + '\n'
        return output

    def damage(self,damage):
        self.health -= damage
