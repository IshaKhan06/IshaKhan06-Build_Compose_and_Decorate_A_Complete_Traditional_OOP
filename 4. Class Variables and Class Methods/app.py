'''Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.'''

class Bank:
    bank_name = "Meezan Bank" 

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")


acc1 = Bank("Isha")
acc2 = Bank("Wasam")

acc1.display()
acc2.display()

Bank.change_bank_name("HBL Bank") 

acc1.display()
acc2.display()
