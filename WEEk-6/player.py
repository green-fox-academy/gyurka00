import random
class Player():
    def __init__(self, name = ''):
        self.name = name
        self.random_stats()
        self.inventory = ['None', 'Leather Armor', 'Sword']

    def player_stats(self):
        return ('Dexterity: ' + str(self.dexterity) + ' , Health: ' + str(self.health) + ' , Luck: ' + str(self.luck))

    def random_stats(self):
        self.dexterity = self.roll() + 6
        self.health = random.randrange(1, 6) + random.randrange(1, 6) + 12
        self.luck = random.randrange(1, 6) + 6
        self.max_dexterity = self.dexterity
        self.max_health = self.health
        self.max_luck = self.luck

    @staticmethod
    def roll():
        number = random.randrange(1, 6)
        return number

    def insert_potion(self, potion):
        del self.inventory[0]
        self.inventory.insert(0, potion)

    def print_monster_stats(self):
        output = ''
        output += 'Max Dexterity: ' + str(self.max_dexterity) + '\n'
        output += 'Current Dexterity: ' + str(self.dexterity) + '\n'
        output += 'Max Health: ' + str(self.max_health) + '\n'
        output += 'Current Health: ' + str(self.health) + '\n'
        return output

    def print_all_stats(self):
        output = ''
        output += 'Namme: ' + str(self.name) + '\n'
        output += self.print_monster_stats()
        output += 'Max Luck: ' + str(self.max_luck) + '\n'
        output += 'Current Luck: ' + str(self.luck) + '\n'
        output += 'Inventory:\n'
        for i in self.inventory:
            output += '\t' + i + '\n'
        return output

    def create_dictionary(self):
        dictionary = {'name' : self.name, 'dexterity' : self.dexterity, 'health' : self.health, 'luck' : self.luck, 'inventory' : [self.inventory[0], self.inventory[1], self.inventory[2]]}
        return dictionary
