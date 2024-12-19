
class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def display_balance(self):
        print("Account Number: ", self.account_number)
        print("Balance: ", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited: ", amount)
        print("New Balance: ", self.balance)
    
    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Withdrawn: ", amount)
            print("New Balance: ", self.balance)

class AccountManager:

    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Account Number: ")
        balance = int(input("Balance: "))
        self.accounts[account_number] = BankAccount(account_number, balance)

    def display_accounts_and_balances(self):
        for account_number, account in self.accounts.items():
            print("Account Number: ", account_number)
            print("Balance: ", account.balance)

    def transfer_money(self, amount, account_number):
        found_account = self.accounts[account_number]
        if (found_account):
            found_account.deposit(amount)
        else:
            print("Account not found")


