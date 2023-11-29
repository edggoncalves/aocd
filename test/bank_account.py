class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __repr__(self):
        return "Account Balance: {}".format(self.balance)

    def deposit(self, amount):
        self.balance += amount


a = BankAccount(1024)
b = BankAccount(42)


result = a.balance + b.balance

print(result)

acc = BankAccount(0)
acc.deposit(int(input()))

print(acc)
