import menu
def reenter_name():
    pass

def new_game_continue():
    pass

def quit():
    pass

def new_game():
    user_name = input('Given a user name: ')
    print(user_name)
    par = [{'name' : 'Reenter name', 'func' : reenter_name}, {'name' : 'Continue', 'func' : new_game_continue},  {'name' : 'Quit', 'func' : quit}]
    new_game = menu.Menu(par)
    print(new_game.menu_list(), end = "")
    selected_menu_item = new_game.choose_list_item()

def load_game():
    print('hutyutyu')

def exit_game():
    exit()


par = [{'name' :'New Game', 'func' : new_game}, {'name' : 'Load Game', 'func' : load_game}, {'name' : 'Exit', 'func' : exit_game}]
main_menu = menu.Menu(par)
print(main_menu.menu_list(), end = "")
selected_menu_item = main_menu.choose_list_item()
if selected_menu_item == 1:
    main_menu.list[selected_menu_item-1]['func']()
if selected_menu_item == 2:
    main_menu.list[selected_menu_item-1]['func']()
elif selected_menu_item == 3:
    main_menu.list[selected_menu_item-1]['func']()
