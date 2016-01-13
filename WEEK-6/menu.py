class Menu():
    def __init__(self, items = None):
        self.items = items

    def menu_list(self):
        output = ""
        for item in self.items:
            output += str(item.num) + ". " + item.name + "\n"
        return output

    def user_input(self):
        while True:
            try:
                sub_menu = int(input("Write the submenu number and press enter: "))
                if not sub_menu or sub_menu < 0 or sub_menu > len(self.items):
                    raise ValueError('')
                else:
                    return sub_menu
            except ValueError:
                print('You entered a wrong value')


    def choose_item_in_items(self):
        item_number = self.user_input()
        for item in self.items:
            if item.num == item_number:
                return item.func()

    def menu_draw(self):
        print(self.menu_list())
        self.choose_item_in_items()
