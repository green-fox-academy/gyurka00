import menu
import player
import character
import os
from roll import *
from stack import Stack
from menu_item import MenuItem
from jsonIO import *

user = player.Player()
monster = character.Character('Diablo')
attack= True
previus_menu = Stack()


def add_new_item():
    name = input('Write file name: ')
    write_json(name, user.create_dictionary())

def resume():
    resume = menu.Menu(previus_menu.return_name())
    resume.menu_draw()

def quit():
    quit_menu_data = [
        MenuItem(1, 'Save and Quit', save_and_quit),
        MenuItem(2, 'Quit without save', quit_without_save),
        MenuItem(3, 'Resume', resume)
        ]
    quit_menu = menu.Menu(quit_menu_data)
    quit_menu.menu_draw()

def save():
    print('\n\n')
    jsons = list_jsons()
    for json in jsons:
        print(json)
    print('\n\n')
    save_menu_data = [
        MenuItem(1, 'Add new item', add_new_item),
        MenuItem(2, 'Resume', resume),
        MenuItem(3, 'Quit', quit)
        ]
    save_menu = menu.Menu(save_menu_data)
    save_menu.menu_draw()

def save_and_quit():
    save()

def quit_without_save():
    return exit()

def strike_sub_menu_continue():
    if attack:
        monster.damage(2)
    else:
        user.damage(2)
    begin()

def strike_sub_menu_luck():
    luck = double_roll()
    if attack:
        if luck > user.luck:
            monster.damage(1)
            user.luck_down()
        else:
            print('You are lucky.')
            monster.damage(4)
            user.luck_down()
    else:
        if luck > user.luck:
            user.damage(3)
            user.luck_down()
        else:
            print('You are lucky.')
            user.damage(1)
            user.luck_down()
    begin()

def strike_sub_menu_retreat():
    pass

def strike_sub_menu():
    strike_sub_menu_data = [
        MenuItem(1, 'Continue', strike_sub_menu_continue),
        MenuItem(2, 'Try your Luck', strike_sub_menu_luck),
        MenuItem(3, 'Retreat', strike_sub_menu_retreat),
        MenuItem(4, 'Quit', quit)
        ]
    strike_sub_menu = menu.Menu(strike_sub_menu_data)
    previus_menu.get_name(strike_sub_menu_data)
    strike_sub_menu.menu_draw()

def strike():
    global attack
    player_roll = double_roll() + user.dexterity
    monster_roll = double_roll() + monster.dexterity
    while player_roll == monster_roll:
        player_roll = double_roll() + user.dexterity
        monster_roll = double_roll() + monster.dexterity
    if player_roll > monster_roll:
        print('You hit the monster ')
        attack = True
        return strike_sub_menu()
    elif player_roll < monster_roll:
        print('The monster hit you ')
        attack = False
        return strike_sub_menu()

def retreat():
    pass

def begin_menu():
    begin_menu_data = [
        MenuItem(1, 'Strike', strike),
        MenuItem(2, 'Retreat', retreat),
        MenuItem(3, 'Quit', quit)
        ]
    begin_menu = menu.Menu(begin_menu_data)
    previus_menu.get_name(begin_menu_data)
    begin_menu.menu_draw()

def begin():
    print('\n---Fight---\n')
    print('User')
    print(user.print_all_stats())
    print('Monster')
    print(monster.print_stats())
    begin_menu()

def potion_continue():
    print(user.print_all_stats())
    potion_continue_menu_data = [
        MenuItem(1, 'Begin', begin),
        MenuItem(2, 'Save', save),
        MenuItem(3, 'Quit', quit)
        ]
    potion_continue = menu.Menu(potion_continue_menu_data)
    previus_menu.get_name(potion_continue_menu_data)
    potion_continue.menu_draw()

def potion_selector(potion):
    user.insert_potion(potion)
    print(user.inventory[0])
    potion_selector_menu_data = [
        MenuItem(1, 'Reselect the Potion', stats_continue),
        MenuItem(2, 'Continue', potion_continue),
        MenuItem(3, 'Quit', quit)
        ]
    selected_potion = menu.Menu(potion_selector_menu_data)
    previus_menu.get_name(potion_selector_menu_data)
    selected_potion.menu_draw()

def stats_continue():
    stats_continue_menu_data = [
        MenuItem(1, 'Potion of Health', potion_selector),
        MenuItem(2, 'Potion of Dexterity', potion_selector),
        MenuItem(3, 'Potion of Luck', potion_selector)
        ]
    potion = menu.Menu(stats_continue_menu_data)
    print(potion.menu_list())
    selected_potion = potion.user_input()
    for item in potion.items:
        if item.num == selected_potion:
            return item.func(item.name)

def reroll_stats():
    return new_game_continue()

def new_game_continue():
    user.random_stats()
    print(user.player_stats())
    new_game_continue_menu_data = [
        MenuItem(1, 'Reroll stats', reroll_stats),
        MenuItem(2, 'Continue', stats_continue),
        MenuItem(3, 'Save', save),
        MenuItem(4, 'Quit', quit)
        ]
    quit_new_game = menu.Menu(new_game_continue_menu_data)
    previus_menu.get_name(new_game_continue_menu_data)
    quit_new_game.menu_draw()

def reenter_name():
    return new_game()

def new_game():
    user_name = input('Given a user name: ')
    user.name = user_name
    print(user.name)
    new_game_menu_data = [
        MenuItem(1, 'Reenter name', reenter_name),
        MenuItem(2, 'Continue', new_game_continue),
        MenuItem(3, 'Save', save),
        MenuItem(4, 'Quit', quit)
        ]

    new_game = menu.Menu(new_game_menu_data)
    previus_menu.get_name(new_game_menu_data)
    new_game.menu_draw()

def load_game():
    print('\n\n')
    jsons = list_jsons()
    for json in jsons:
        print(json)
    print('\n\n')
    name = input('Write file name: ')
    data = load_json(name)
    user.load_dictionary(data)
    potion_continue()


def exit_game():
    exit()

def main():
    main_menu_data = [
        MenuItem(1, 'New Game', new_game),
        MenuItem(2, 'Load Game', load_game),
        MenuItem(3, 'Exit', exit)
        ]
    main_menu = menu.Menu(main_menu_data)
    main_menu.menu_draw()
