import menu
from menu_item import MenuItem
import player
import character
import json

user = player.Player()
monster = character.Character()

def save():
    data_file = open('data.json', 'w')
    json.dump(user.create_dictionary(), data_file)
    data_file.close()

def strike_sub_menu_continue():
    pass

def strike_sub_menu_luck():
    pass

def strike_sub_menu_retreat():
    pass

def strike_sub_menu_quite():
    pass

def strike_sub_menu(who):
    par = [
        MenuItem(1, 'Continue', strike_sub_menu_continue),
        MenuItem(2, 'Try your Luck', strike_sub_menu_luck),
        MenuItem(3, 'Retreat', strike_sub_menu_retreat),
        MenuItem(4, 'Quit', strike_sub_menu_quite)
        ]
    strike_sub_menu = menu.Menu(par)
    strike_sub_menu.menu_draw()

def strike():
    player_roll = user.roll() + user.roll()
    monster_roll = monster.roll() + monster.roll()
    if player_roll > monster_roll:
        print('You hit the monster')
        return strike_sub_menu(monster)
    elif player_roll == monster_roll:
        print('You are lucky.')
        return strike()
    else:
        print('The monster hit you')
        return strike_sub_menu(user)

def retreat():
    pass

def begin_quite():
    pass

def begin_menu():
    par = [
        MenuItem(1, 'Strike', strike),
        MenuItem(2, 'Retreat', retreat),
        MenuItem(3, 'Quit', begin_quite)
        ]
    potion_continue = menu.Menu(par)
    potion_continue.menu_draw()

def begin():
    print('\n---Test Fight---\n')
    print('User')
    print(user.print_all_stats())
    print('Monster')
    print(monster.print_stats())
    begin_menu()

def potion_continue_quite():
    return stats_continue()

def potion_continue():
    print(user.print_all_stats())
    par = [
        MenuItem(1, 'Begin', begin),
        MenuItem(2, 'Save', save),
        MenuItem(3, 'Quit', potion_continue_quite)
        ]
    potion_continue = menu.Menu(par)
    potion_continue.menu_draw()

def potion_quite():
    return stats_continue()


def potion_selector(potion):
    user.insert_potion(potion)
    print(user.inventory[0])
    par = [
        MenuItem(1, 'Reselect the Potion', stats_continue),
        MenuItem(2, 'Continue', potion_continue),
        MenuItem(3, 'Quit', potion_quite)
        ]
    selected_potion = menu.Menu(par)
    selected_potion.menu_draw()



def stats_continue():
    par = [
    MenuItem(1, 'Potion of Health', potion_selector),
    MenuItem(2, 'Potion of Dexterity', potion_selector),
    MenuItem(3, 'Potion of Luck', potion_selector)
    ]
    potion = menu.Menu(par)
    print(potion.menu_list())
    selected_potion = potion.user_input()
    for item in potion.items:
        if item.num == selected_potion:
            return item.func(item.name)

def reroll_stats():
    return new_game_continue()

def quite_to_new_game():
    return new_game()

def new_game_continue():
    user.random_stats()
    print(user.player_stats())
    par = [
        MenuItem(1, 'Reroll stats', reroll_stats),
        MenuItem(2, 'Continue', stats_continue),
        MenuItem(3, 'Save', save),
        MenuItem(4, 'Quit', quite_to_new_game)
        ]
    quit_new_game = menu.Menu(par)
    quit_new_game.menu_draw()


def save_and_quite():
    save()
    return main()

def quite_without_save():
    return main()

def resume():
    return new_game_continue()

def quit_to_main():
    par = [
        MenuItem(1, 'Save and Quit', save_and_quite),
        MenuItem(2, 'Quit without save', quite_without_save),
        MenuItem(3, 'Resume', resume)
        ]
    quit_new_game = menu.Menu(par)
    quit_new_game.menu_draw()

def reenter_name():
    return new_game()

def new_game():
    user_name = input('Given a user name: ')
    user.name = user_name
    print(user.name)
    par = [
        MenuItem(1, 'Reenter name', reenter_name),
        MenuItem(2, 'Continue', new_game_continue),
        MenuItem(3, 'Save', save),
        MenuItem(4, 'Quit', quit_to_main)
        ]
    new_game = menu.Menu(par)
    new_game.menu_draw()

def load_game():
    print('Load Game')

def exit_game():
    exit()

def main():
    par = [
        MenuItem(1, 'New Game', new_game),
        MenuItem(2, 'Load Game', load_game),
        MenuItem(3, 'Exit', exit)
        ]
    main_menu = menu.Menu(par)
    main_menu.menu_draw()

main()
