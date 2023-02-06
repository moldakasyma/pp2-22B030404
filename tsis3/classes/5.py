class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        
    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance:{self.balance}'
    def deposit(self,dep):
        self.balance+=dep
        print('Deposit accepted')
    def withdraw(self,wd):
        if self.balance>=wd:
            self.balance-=wd
            print('Withdrawal accepted')
        else:
            print('Funds Unavailable!')
a=Account('Aiya',100000)
print(a)
print(a.owner)
print(a.withdraw(90))
print(a.balance)
        