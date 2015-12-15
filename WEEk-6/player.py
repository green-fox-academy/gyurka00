import random
class Player():
    def __init__(self, name = ''):
        self.name = name
        self.random_stats()
        self.inventory = ['', 'Leather Armor', 'Sword']

    def player_stats(self):
        return ('Dexterity: ' + str(self.dexterity) + ' , Health: ' + str(self.health) + ' , Luck: ' + str(self.luck))

    def random_stats(self):
        self.dexterity = random.randrange(1, 6) + 6
        self.health = random.randrange(1, 6) + random.randrange(1, 6) + 12
        self.luck = random.randrange(1, 6) + 6

    def insert_potion(self, potion):
        del self.inventory[0]
        self.inventory.insert(0, potion)

    def print_all_stats(self):
        output = ''
        output += 'Dexterity: ' + str(self.dexterity) + '\n'
        output += 'Health: ' + str(self.health) + '\n'
        output += 'Luck: ' + str(self.luck) + '\n'
        output += 'Inventory:\n'
        for i in self.inventory:
            output += '\t' + i + '\n'
        return output
