#commentid code with some example just for me
'''balance = 0

def deposit(amount):
    global balance
    balance+=amount
    return balance

def withdraw(amount):
    global balance
    balance-=amount
    return balance
'''
'''def make_account():
    return {'balance':0}

def deposit(account, amount):
    account['balance']+=amount
    return account['balance']

def withdrew(account, amount):
    account['balance']-=amount
    return account['balance']'''

#real code start
class bank_account:
    def __init__(self, name, balance = 0):
        self.balance = balance
        self.name = name


    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdrew(self, amount):
        self.balance -= amount
        return self.balance
