default_table = [[1,1,0,1,0,0,1,1,1,1],
            [0,0,0,1,0,0,0,0,0,0],
            [1,0,0,1,0,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,1,0,0,0,1],
            [0,0,0,0,0,1,0,0,0,1],
            [1,1,0,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,1,1,1,1,1]]

class Table:
    def __init__(self, table = default_table):
        self.table = table
        self.lives = 31

    def ready(self):
        return True

    def drav_table(self):
        for n in self.table:
            print(n)

    def attack(self,row,col):
        if self.table[row][col] == 1:
            self.lives -= 1
            return True
        else:
            return False

    def is_win(self):
        if self.lives == 0:
            return True
        else:
            return False


# a = Table()
# a.drav_table()
