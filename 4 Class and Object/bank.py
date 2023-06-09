class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'After deposite. your balance is {self.balance}')

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            # return f'Fokirra!!! You can not withdraw below {self.min_withdraw}' evabeo korte partam kintu arekta varible e niye nite hobe
            print(
                f'Fokirra!!! You can not withdraw below {self.min_withdraw} because your demandable balance is {amount}')
        elif amount > self.max_withdraw:
            # return f'Bank fokir hoye jabe. You can not with more than {self.max_withdraw}' same ager motoi
            print(
                f'Bank fokir hoye jabe. You can not with more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'here is your money {amount}')
            print(f'Your balance after withdraw is {self.balance}')


Brac = Bank(15000)
Brac.withdraw(99)
Brac.deposite(100)
Brac.withdraw(10000)

DBBL = Bank(10000)
DBBL.withdraw(90)
DBBL.deposite(10000)
DBBL.withdraw(9000)
