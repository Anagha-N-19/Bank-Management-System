def transferamount(customers):
    print("You can transfer an amount from your account to requested account")
    c1=int(input("Enter your account number "))
    c2=int(input("Enter recepient's account number "))
    t=int(input("Enter amount "))
    bc[c1].total=bc[c1].total-t
    bc[c2].total=bc[c1].total+t
    print("Your Current Balance =",bc[c1].total)
    print("Recepient's Current Balance =",bc[c2].total)
def acccreate():
    cname=input("Enter name ")
    accno=int(input("Enter account number "))
    bc[accno]=Bank(cname,accno)
    print("New account created with initial deposit of Rs 500")
    return bc
class Bank():
    def __init__(self, name="Invalid",accno=0):
        self.name=name
        self.accno=accno
        self.total=500
    def withdraw(self,m):
        if m<self.total:
            self.total=self.total - m
            print("Amount withdrawn")
            print("Current balance is",self.total)
        else:
            print("Inadequate balance")
    def deposit(self, m):
        self.total+=m
        print("Current Balance =",self.total)
    def balance(self):
        print("Name of Account holder :",self.name)
        print("Account no :",self.accno)
        print("Current balance = ",self.total)
        if self.total<2000:
            print("Inadequate Balance")
    def dets(self):
        print("Name of Account holder :",self.name)
        print("Account no :",self.accno)
        print("Current balance =",self.total)
p=True
bc={}
print("1-New account creation \n2-Deposit\n3-Withdraw\n4-Check balance\n5-Transfer amount\n6-Search account")
while p==True:
            n=int(input())
            if n==1:
                acccreate()
            elif n==2:
                accno=int(input("Enter account number "))
                m=int(input("Enter amount to be deposited "))
                bc[accno].deposit(m)
            elif n==3:
                accno=int(input("Enter account number "))
                amt=int(input("Enter amount to be withdrawn "))
                bc[accno].withdraw(amt)
            elif n==4:
                accno=int(input("Enter account number "))
                bc[accno].balance()
            elif n==5:
                transferamount(bc)
            elif n==6:
                no=int(input("Enter account number "))
                bc[no].dets()
            else:
                p=False
                
