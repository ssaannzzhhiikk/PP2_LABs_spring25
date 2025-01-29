class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, summa):
        if summa > 0:
            self.balance += summa
            print(f"Transaction was successful, new balance: {self.balance}")
        else:
            print("Invalid number, please insert real amount!")
    def withdraw(self, summa):
        if summa > self.balance or summa <= 0:
            print("Invalid withdrawal")
        else:
            self.balance -= summa
            print(f"Successful withdrawal, Your balance now: {self.balance}")

    def __str__(self):
        return f"Account(owner='{self.owner}', balance=₸{self.balance:.2f})"


acc = Account("Sanzhar", 2500)
print(acc)

acc.deposit(500)
acc.deposit(-2)
print(acc)

acc.withdraw(200)
acc.withdraw(-23)
print(acc)
