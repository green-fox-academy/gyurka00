import menu
from menu_item import MenuItem
import player

user = player.Player()

def save():
    print('save')

def reenter_name():
    return new_game()

def reroll_stats():
    return new_game_continue()

def stats_quite():
    print('stats_quite')

def begin():
    pass

def potion_continue_save():
    pass

def potion_continue_quite():
    pass

def potion_continue():
    print(user.print_all_stats())
    par = [
        MenuItem(1, 'Begin', begin),
        MenuItem(2, 'Save', potion_continue_save),
        MenuItem(3, 'Quit', potion_continue_quite)
        ]
    potion_continue = menu.Menu(par)
    potion_continue.menu_draw()
    Begin, Save, Quit

def potion_quite():
    print('potion_quite')

def potion_selector(potion):
    user.insert_potion(potion)
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


def new_game_continue():
    user.random_stats()
    print(user.player_stats())
    par = [
        MenuItem(1, 'Reroll stats', reroll_stats),
        MenuItem(2, 'Continue', stats_continue),
        MenuItem(3, 'Save', save),
        MenuItem(4, 'Quit', stats_quite)
        ]
    quit_new_game = menu.Menu(par)
    quit_new_game.menu_draw()


def save_and_quite():
    print('save_and_quite')

def quite_without_save():
    pass

def resume():
    pass

def quit():
    par = [
        MenuItem(1, 'Save and Quit', save_and_quite),
        MenuItem(2, 'Quit without save', quite_without_save),
        MenuItem(3, 'Resume', resume)
        ]
    quit_new_game = menu.Menu(par)
    quit_new_game.menu_draw()

def new_game():
    user_name = input('Given a user name: ')
    user.name = user_name
    print(user.name)
    par = [
        MenuItem(1, 'Reenter name', reenter_name),
        MenuItem(2, 'Continue', new_game_continue),
        MenuItem(3, 'Save', save),
        MenuItem(4, 'Quit', quit)
        ]
    new_game = menu.Menu(par)
    new_game.menu_draw()

def load_game():
    print('hutyutyu')

def exit_game():
    exit()

par = [
    MenuItem(1, 'New Game', new_game),
    MenuItem(2, 'Load Game', load_game),
    MenuItem(3, 'Exit', exit)
    ]
main_menu = menu.Menu(par)
main_menu.menu_draw()
