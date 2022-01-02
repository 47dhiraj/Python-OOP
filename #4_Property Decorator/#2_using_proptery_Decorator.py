class Employee:                                         # Employee is class

    def __init__(self, first, last):                    # self keyword represents the instance or object in python # constructor ho
        self.first = first                              # self.variable represents the instance variable ,,,, instance variable values are different for different instances
        self.last = last                                # self.variable represents the instance variable ,,,, instance variable values are different for different instances

    @property                                           # kunai method mathi @property decorator use gare pachi tyo method le property or attribute jasari kaam garcha
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property                                           # kunai method mathi @property decorator use gare pachi tyo method le property or attribute jasari kaam garcha
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# Note : kunai method ma property decorator use garnu ko pahilo faida vaneko timile method lai property jasari use garna sakchau & 2nd imp faida vaneko kunai instance variable ko latest or updated value lai access garna sakchau


emp_1 = Employee('Johnny', 'Doey')                      # creating a object of Employee class

emp_1.first = 'John'                                    # instance variable value being changed or updated
emp_1.last = 'Doe'                                      # instance variable value being changed or updated

print(emp_1.email)                                      # we are able to call email method as like property  # yesari method lai as property call garna sakyo vani kunai pani instance variable ko latest or updated value lina sakincha
print(emp_1.fullname)                                   # we are able to call fullname method as like property  # yesari method lai as property call garna sakyo vani kunai pani instance variable ko latest or updated value lina sakincha



