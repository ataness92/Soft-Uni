class Account:

    def __init__(self, _id: int, name: str, balance: int = 0):
        self.id = _id
        self.name = name
        self.balance = balance


    def credit(self, amount):
        self.balance += amount
        return self.balance


    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return f"Amount exceeded balance"


    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"