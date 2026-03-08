#wrapping data and code together into a single unit (object) is called encapsulation


class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.accountnumber = acc

    def debit(self, amount):
        self.balance -= amount    
        print("Amount debited: ", amount)
        print("Balnce decreased to : ", self.balance)

    def credit(self, amount):
        self.balance += amount    
        print("Amount credited: ", amount)
        print("Balnce increased to : ", self.balance)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.accountnumber

acc1 = account (1000, 5468)
acc1.debit(500)
acc1.credit(200)