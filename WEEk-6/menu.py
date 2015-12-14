class Menu():
    def __init__(self, lst = None):
        self.list = lst

    def __repr__(self):
        return {}.format()

    def menu_list(self):
        output = ""
        i = 1
        for dictionary in self.list:
            output += str(i) + ". " + dictionary['name'] + "\n"
            i += 1
        return output

    def choose_list_item(self):
        try:
            sub_menu = int(input("Write the submenu number and press enter: "))
            if not sub_menu or sub_menu > len(self.list):
                raise ValueError('')
        except ValueError:
            print('You entered a wrong value')
            self.choose_list_item()
        return sub_menu

    def menu_draw(self):
        print(self.menu_list(), end = "")
        selected_menu_item = main_menu.choose_list_item()
