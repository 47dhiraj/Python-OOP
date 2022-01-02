#class vitra ko variable lai protected banauna ko lagi single '_' (underscore) lekhinxa

#private member lai tyo class vanda bahira kahi batw pani access garna paidaina..i.e child class batw pani access garna paidaina

class Employee:
    def __init__(self, name):
        self._salary = 2000
        self.name = name

class BankEmployee(Employee):

    def show(self):
        print(self._salary)

e1 =BankEmployee("Ram")

e1.show()  
print(e1._salary) #protected lai yesari bahira batw object banayera pani protected variable lai access garna sakinxa    #we should not do this.