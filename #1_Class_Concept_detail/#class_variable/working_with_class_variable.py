class Employee:
    # just class vitra (i.e constructor or any methods vanda mathi self.  use nagari declare garni variable lai class variable vanincha)
    # class variable kunai auta particular object sanga related hune khalko variable chai hoina... class variable tw class sanga matra related hune khalko variable ho
    num_of_emps = 0
    raise_amt = 1.5

    def __init__(self, first, last, pay, raise_amout= None):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1                               # Class variable lai class. garera access garna sakincha..  self.  gari rakhna pardaina
        if raise_amout != None:
            self.raise_amt = raise_amout


    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)                 # yedi particular object anusar class variable ko value farak farak cha vani self. garera nai class variable ko value access garni
        # self.pay = int(self.pay * Employee.raise_amt)           # yedi sabbai employee object lai class variable ko value same nai huncha vanni 100% fix nai cha vani,  class. garera class variable ko value access gare huncha....
        return self.pay


# For checking the no. of objects created
print('Number of Employees :', Employee.num_of_emps)

# yedi sabbai employee object lai same raise amout nai huncha vani 100% fix cha vani, object create garda nai farak farak raise amout pathai rakhnai parena.. clas variable ma j raise amout value cha tei nai use huncha
# emp_1 = Employee('John', 'Doe', 50000)
# emp_2 = Employee('Agent', '47', 50000)

# # print(Employee.__dict__)                                        # Class ko namespace check garni tarika

# print(emp_1.__dict__)                                           # particular object ko namespace check garni tarika
# print(emp_2.__dict__)                                           # particular object ko namespace check garni tarika
#
# print(emp_1.apply_raise())
# print(emp_2.apply_raise())




# yedi kunai employee lai raise amout garni kunai lai nagarni ho vani yesari employee object banaudai kunai lai raise amout halera banaune, kunai lai na hali banaune
emp_1 = Employee('John', 'Doe', 50000, 2)           # yedi, employee object create garda nai specific raise amount halera create gareko cha vani, so yesle class variable ma vako initial  1.5  raise_amount vanni value lai override garera 2 garaucha
emp_2 = Employee('Agent', '47', 50000)              # yedi, employee object create garda nai specific raise amount halera create gareko chaina vani, so yesle class variable ma vako initial  1.5  raise_amount nai ligi rakhya huncha

# print(Employee.__dict__)

print(emp_1.__dict__)
print(emp_1.raise_amt)
print(emp_1.apply_raise())

print(emp_2.__dict__)
print(emp_2.raise_amt)
print(emp_2.apply_raise())




# At Final, checking the no. of employees created
print('Number of Employees :', Employee.num_of_emps)