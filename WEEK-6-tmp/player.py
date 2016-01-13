import random
import character
from roll import *

class Player(character.Character):
    def __init__(self, name = ''):
        super().__init__(name)
        self.inventory = ['None', 'Leather Armor', 'Sword']

    def player_stats(self):
        return ('Dexterity: ' + str(self.dexterity) + ' , Health: ' + str(self.health) + ' , Luck: ' + str(self.luck))

    def random_stats(self):
        super().random_stats()
        self.luck = roll() + 6
        self.max_luck = self.luck

    def insert_potion(self, potion):
        del self.inventory[0]
        self.inventory.insert(0, potion)

    def print_all_stats(self):
        output = ''
        output += self.print_stats()
        output += 'Max Luck: ' + str(self.max_luck) + '\n'
        output += 'Current Luck: ' + str(self.luck) + '\n'
        output += 'Inventory:\n'
        for i in self.inventory:
            output += '\t' + i + '\n'
        return output

    def create_dictionary(self):
        dictionary = {'name' : self.name, 'dexterity' : self.dexterity, 'health' : self.health, 'luck' : self.luck,'max_dexterity' : self.max_dexterity, 'max_health' : self.max_health, 'max_luck' : self.max_luck, 'inventory' : [self.inventory[0], self.inventory[1], self.inventory[2]]}
        return dictionary

    def load_dictionary(self, dictionary):
        self.name = dictionary['name']
        self.dexterity = dictionary['dexterity']
        self.health = dictionary['health']
        self.luck = dictionary['luck']
        self.max_dexterity = dictionary['max_dexterity']
        self.max_health = dictionary['max_health']
        self.max_luck = dictionary['max_luck']
        del self.inventory[2]
        del self.inventory[1]
        del self.inventory[0]
        self.inventory.insert(0, dictionary['inventory'][0])
        self.inventory.insert(1, dictionary['inventory'][1])
        self.inventory.insert(2, dictionary['inventory'][2])

    def luck_down(self):
        self.luck -= 1
