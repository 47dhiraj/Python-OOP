# Private members

class Employee:
    def __init__(self, name):
        self.__salary =2000 #protected member(varibale) banauna double underscore lekhinxa '__'
        self.name = name


e1 = Employee("Ram")

#print(e1.__salary)  #protected member lai yesari bahira object banayera access garna paidaina... error aauxa

