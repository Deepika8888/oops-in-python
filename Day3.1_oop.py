#lets learn about private attributes 

class BankAccount: 
    def __init__(self, balance):
        self._balance = balance #private attribute, _ makes the attribute private
        
    def show_balance(self):
        print(f"Your current balance is {self._balance}")
    
account = BankAccount(1000)
account.show_balance()
#print(account.balance) won't work here. 