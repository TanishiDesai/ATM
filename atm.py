class ATM(object) :
    def __init__(self, pin, cardNumber, balance) :
     self.pin = pin
     self.cardNumber = cardNumber
     self.balance = balance
    def CashWithdrawl(self):
        print("Cast is withdrawed")
    def  BalanceEnquiry(self):
        print("Thish is your blance :" + balance )
Tanishi = ATM("3236", "23xxxxx20", "1,50,000")
print(Tanishi.balance)
















      

