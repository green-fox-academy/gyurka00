from roll import *
class Character():
    def __init__(self, name = ''):
        self.name = name
        self.random_stats()

    def random_stats(self):
        self.dexterity = roll() + 6
        self.health = roll() + roll() + 12
        self.max_dexterity = self.dexterity
        self.max_health = self.health

    def print_stats(self):
        output = ''
        output += 'Namme: ' + str(self.name) + '\n'
        output += 'Max Dexterity: ' + str(self.max_dexterity) + '\n'
        output += 'Current Dexterity: ' + str(self.dexterity) + '\n'
        output += 'Max Health: ' + str(self.max_health) + '\n'
        output += 'Current Health: ' + str(self.health) + '\n'
        return output

    def damage(self,damage):
        print(self.name, '     ', self.health)
        self.health -= damage
