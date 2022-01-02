class Employee:

    def __init__(self, first, last, pay):           # __init__ vannale constructor ho
        self.first = first                          # self.variable vannale instance variable or object variable vanne bujincha.... yeso varibale le particular object ko lagi alag alag memory reference garne garcha & farak farak values hold garne garcha
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        # instance variable are actually unique for each instance or object

    def fullname(self):                             # since function lai jahile pani object le nai call gari rako huncha, so tei vayera jahile pani function ma self vanni parameter tw hunai parcha
        return '{} {}'.format(self.first, self.last)



emp_1 = Employee('John', 'Doe', 50000)              # creating instance or object of Employee class

emp_2 = Employee('Agent', '47', 60000)              # creating instance or object of Employee class



# print(id(emp_1.first))                            # particular object ko particular variabale ko memory location check garni tarika
print(emp_1.first)
print(emp_1.fullname())
# Alternative way of calling method inside class
# print(Employee.fullname(emp_1))

# print(id(emp_2.first))                            # particular object ko particular variabale ko memory location check garni tarika
print(emp_2.first)
print(emp_2.fullname())
# Alternative way of calling method inside class
# print(Employee.fullname(emp_2))
