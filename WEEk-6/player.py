import random
import character
class Player(character.Character):
    def __init__(self, name = ''):
        super().__init__(name)
        self.inventory = ['None', 'Leather Armor', 'Sword']

    def player_stats(self):
        return ('Dexterity: ' + str(self.dexterity) + ' , Health: ' + str(self.health) + ' , Luck: ' + str(self.luck))

    def random_stats(self):
        super().random_stats()
        self.luck = self.roll() + 6
        self.max_luck = self.luck

    def insert_potion(self, potion):
        del self.inventory[0]
        self.inventory.insert(0, potion)

    def print_all_stats(self):
        output = ''
        output += 'Namme: ' + str(self.name) + '\n'
        output += self.print_stats()
        output += 'Max Luck: ' + str(self.max_luck) + '\n'
        output += 'Current Luck: ' + str(self.luck) + '\n'
        output += 'Inventory:\n'
        for i in self.inventory:
            output += '\t' + i + '\n'
        return output

    def create_dictionary(self):
        dictionary = {'name' : self.name, 'dexterity' : self.dexterity, 'health' : self.health, 'luck' : self.luck, 'inventory' : [self.inventory[0], self.inventory[1], self.inventory[2]]}
        return dictionary
