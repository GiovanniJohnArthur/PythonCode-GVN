class BankAccount:
    def __init__(self, name, balance=0):
        self.account_holder = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount} to your account")

    def withdraw(self, amount):
        if amount > self.balance:
            print('Not enough balance')
        else:
            self.balance = self.balance - amount
            print(f"Successful withdrew {amount} from your account")

    def __str__(self):
        return f"Account Holder Name: {self.account_holder} \nBalance: {self.balance}"


obj = BankAccount('John', 1000)
print(obj)
obj.deposit(200)
obj.withdraw(800)
print(obj.balance)