
class MyMagic:
    def __init__(self,names = []):
        self.names = names

    def lists_names(self):
        return list(map(lambda name: name['name'], self.names))

    def names_start_with_j(self):
        return list(filter(lambda name: name[0] == 'J', self.lists_names()))
