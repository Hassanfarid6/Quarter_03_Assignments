# 4. Class Variables and Class Methods Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) 
# that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "HBL"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


    @classmethod
    def display_bank(cls):
        print(f"Create Account in {cls.bank_name}")

# creating Instance
banks = Bank()
Bank.display_bank()

Bank.change_bank_name("UBL")
Bank.display_bank()