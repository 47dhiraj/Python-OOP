#real world example of method overriding
class Bank:  
    def get_interest_rate(self):  
        return 10

class SBI(Bank):  
    def get_interest_rate(self):  
        return 7  
  
class ICICI(Bank):  
    def get_interest_rate(self):  
        return 8  

class Nabil(Bank):
    pass

b1 = Bank()  
b2 = SBI()  
b3 = ICICI()  
b4 = Nabil()
print("Bank Rate of interest:",b1.get_interest_rate())
print("SBI Rate of interest:",b2.get_interest_rate())  
print("ICICI Rate of interest:",b3.get_interest_rate()) 
print("Nabil Rate of interest:",b4.get_interest_rate())