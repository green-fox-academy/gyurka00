class Bank_account:
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance

    def pay(self,amount):
        self.balance -= amount

    def receive(self,amount):
        self.balance += amount

    def print_balance(self):
        print(self.name + ': ' + str(self.balance))

    def transfer(self,you, amount):
        self.pay(amount)
        you.receive(amount)

abc = Bank_account('tihi',1000)
abc.print_balance()
abc.pay(100)
abc.print_balance()
abc.receive(1000)
abc.print_balance()
cba = Bank_account('tahó',100000)
abc.print_balance()
cba.print_balance()
abc.transfer(cba, 1000)
abc.print_balance()
cba.print_balance()
