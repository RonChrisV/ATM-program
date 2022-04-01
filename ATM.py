import sys

#Python program for an ATM

class Bank_Account:
    def __init__(self,user,account_number):
        self.user = user
        self.account_number = account_number
        self.balance = 0
        print("\n ----------------Welcome To XYZ Bank----------------")
    
    def deposit(self):
        amount=float(input("\n Enter Amount To Be Deposited(₹): "))
        self.balance += amount
        print("\n₹",amount, "has been deposited","\n Current Balance:",self.balance)
                     
    def withdraw(self):
        amount=float(input("\n Enter Amount To Be Withdrawn(₹): "))
        if self.balance>=amount:
            self.balance -= amount
            print("\n₹",amount, "has been withdrawn","\n Current Balance:",self.balance)
        else:
            print("\ Current Balance Insufficient")

    def show_details(self):
        print("\n ACCOUNT DETAILS \n \n Name =",self.user,"\n Account Number=",self.account_number,)

    def options(self):
        print("\n Please Select An Option By Entering 1,2,3,4 or 5: \n 1. Account Detail \n 2. Check Balance \n 3. Deposit \n 4. Withdraw \n 5. Exit")
        while True:
            try:
                option = int(input("\n Enter 1, 2, 3, 4 or 5:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!")
                continue
            else:
                if option == 1:
                    acc.show_details()
                elif option == 2:
                    print("\n Current Balance=₹",self.balance)
                elif option == 3:
                    acc.deposit()
                elif option == 4:
                    acc.withdraw()
                elif option == 5:
                    print("\n ------------Thank You For Using XYZ Bank------------")
                    sys.exit()
                    
acc = Bank_Account("Ronan Varghese",123456789)
PIN = 1234
print("Enter your PIN")
while True:
    accpin = int(input())
    if accpin == PIN:
        acc.options()
    else:
        print("Invalid PIN, retry")
    continue
    

        


