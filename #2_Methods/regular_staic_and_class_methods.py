class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):                   # self keywrod refers to the object
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):                                     # yo chai regular method ho.. regular method ma jahile pani self huncha as first parameter (i.e object as first parameter)
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):                                  # regular method ho & regular method ma jahile pani self (i.e instance or object) as first parameter
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):                          # class method ma jahile pani first parameter class pass garna parcha (i.e cls represent class ) # cls keyword in this class refers to the Employee class
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):                           # class method ma jahile pani first parameter class pass garna parcha (i.e cls represent class ) or automatically class pass nai huncha
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):                                     # static method ma neither pass self nor pass class(i.e cls) as parameter
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# classmethod can be called from class itself.. no need to create object of the class ... Calling class method using Class
Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)




emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# calling the class method
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)


import datetime
my_date = datetime.date(2016, 7, 11)
# Calling static method just using class name itself ...static method can be directly call without creating object..
print(Employee.is_workday(my_date))


