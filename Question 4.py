class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited $",amount," into account ",self.account_number," New balance: $",self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrew $",amount," from account ",self.account_number," New balance: $",self.balance)
        else:
            print("Insufficient funds in account ",self.account_number," Current balance: $",self.balance)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return( "Account Number:" + str(self.account_number) + "Account Holder:" + str(self.account_holder) +" Balance: $" + str(self.balance))

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print("Interest of $",interest_amount," applied to account", self.account_number,". New balance: $",self.balance)

    def __str__(self):
        return (super().__str__() + ", Interest Rate:"+ str(self.interest_rate))

bank_account = BankAccount("26022602", "adham taha")
bank_account.deposit(1000.0)
bank_account.withdraw(500.0)
print(bank_account)
savings_account = SavingsAccount("12123434", "Jane Smith", 1000.0, 0.05)
savings_account.apply_interest()
print(savings_account)