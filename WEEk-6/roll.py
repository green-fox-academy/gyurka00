import random

def roll():
    number = random.randrange(1, 6)
    return number

def double_roll():
    number = roll() + roll()
    return number
