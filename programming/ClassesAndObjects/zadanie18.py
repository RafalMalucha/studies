class bank_acc():
    
    def __init__(self, acc_no):
        self.number = acc_no
        self.balance = 0
        
    def deposit(self, dpst):
        self.balance += dpst
        
    def withdraw(self, wthdrw):
        if self.balance < wthdrw:
            print("Insufficient funds on the account")
        else:
            self.balance -= wthdrw
            
    def disp_balance(self):
        print(f"Balance: {self.balance} PLN")
        
    def disp_details(self):
        print(f"Bank Account No: {self.number}")
        print(f"Balance: {self.balance} PLN")
        
account = bank_acc("12 3456 5555 9090 1111 0000 7722")
account.disp_details()
account.deposit(555.35)
account.disp_balance()
account.withdraw(42.77)
account.disp_balance()
account.withdraw(3333)
account.disp_details()

        