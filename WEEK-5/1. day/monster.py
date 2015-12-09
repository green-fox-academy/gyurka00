from character import Character

class Monster(Character):
    def stiker(self,opponent):
        self.hp +=2
        super().strike(opponent)
