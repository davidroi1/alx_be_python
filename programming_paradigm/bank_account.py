class BankAccount:
    def __init__(self, account_balance=0) -> None:
        self.account_balance = account_balance

    def deposit(self, amount) -> None:
        self.account_balance += amount

    def withdraw(self, amount) -> bool:
        if self.account_balance > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f'Current Balance: ${self.account_balance:.2f}')
