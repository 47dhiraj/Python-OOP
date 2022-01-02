#calling parent's constructor from child class construcotr

class Employee:
    def __init__(self):
        self.salary = 2000


class BankEmployee(Employee):
    def __init__(self, name):
        super().__init__()        # yedi parent class ko purai constructor nai inherit garnu cha vani yesari garna sakincha (yesto bela parent class ko attribute as well as tesma vayeko value both inherit huncha)
        self.name = name


emp = BankEmployee("Ram")
print(emp.name)
print(emp.salary)



