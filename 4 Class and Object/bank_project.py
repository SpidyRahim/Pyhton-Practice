class Bank:
    def __init__(self):
        self.accounts = {}
        self.total_balance = 0
        self.total_loan = 0
        self.loan_enabled = True

    def create_account(self, name):
        if name in self.accounts:
            print("Account already exists")
        else:
            self.accounts[name] = 0
            print("Account created successfully")

    def deposit(self, name, amount):
        if name not in self.accounts:
            print("Account does not exist")
        else:
            self.accounts[name] += amount
            self.total_balance += amount
            print("Amount deposited successfully")

    def withdraw(self, name, amount):
        if name not in self.accounts:
            print("Account does not exist")
        elif amount > self.accounts[name]:
            print("Insufficient balance")
        else:
            self.accounts[name] -= amount
            self.total_balance -= amount
            print("Amount withdrawn successfully")

    def transfer(self, sender, receiver, amount):
        if sender not in self.accounts or receiver not in self.accounts:
            print("Account does not exist")
        elif amount > self.accounts[sender]:
            print("Insufficient balance")
        else:
            self.accounts[sender] -= amount
            self.accounts[receiver] += amount
            print("Amount transferred successfully")

    def check_balance(self, name):
        if name not in self.accounts:
            print("Account does not exist")
        else:
            print("Available balance:", self.accounts[name])

    def take_loan(self, name):
        if name not in self.accounts:
            print("Account does not exist")
        elif not self.loan_enabled:
            print("Loan feature is currently disabled")
        else:
            loan_amount = self.accounts[name] * 2
            self.accounts[name] += loan_amount
            self.total_loan += loan_amount
            print("Loan taken successfully")

    def check_transaction_history(self, name):
        if name not in self.accounts:
            print("Account does not exist")
        else:
            print("Transaction history:")
            # TODO: Implement transaction history


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def check_total_balance(self):
        print("Total available balance:", self.bank.total_balance)

    def check_total_loan(self):
        print("Total loan amount:", self.bank.total_loan)

    def enable_loan(self):
        self.bank.loan_enabled = True
        print("Loan feature enabled")

    def disable_loan(self):
        self.bank.loan_enabled = False
        print("Loan feature disabled")


# Example usage
bank = Bank()
admin = Admin(bank)

bank.create_account("Alice")
bank.deposit("Alice", 1000)
bank.check_balance("Alice")

bank.create_account("Bob")
bank.transfer("Alice", "Bob", 500)
bank.check_balance("Alice")
bank.check_balance("Bob")

bank.take_loan("Alice")
bank.check_balance("Alice")

admin.check_total_balance()
admin.check_total_loan()
admin.disable_loan()
bank.take_loan("Alice")
