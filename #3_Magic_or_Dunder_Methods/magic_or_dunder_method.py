class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):                                         # regular instance method ho
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):                                      # regular instance method ho
        self.pay = int(self.pay * self.raise_amt)


    def __repr__(self):                                         # __repr__()   magic or dunder method ho, it is generally used for debugging purpose by the developer
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):                                          # __str__()  magic or dunder method ho, it is called when print() or str() method is called & it is used for the redable representation of the object
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):                                   # __add__()  magic or dunder method ho, it is called after + operation between the objects
        return self.pay + other.pay

    def __len__(self):                                          # __len__()  magic or dunder method ho, it is called for finding the length of the object
        return len(self.fullname())


emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jimmy', 'Jimmer', 60000)


# for use of __repr__() magic method
print(repr(emp_1))
print(emp_1.__repr__())
print(repr(emp_2), '\n')
print(emp_2.__repr__())


# for use of __str__() magic method
print(emp_1)
print(str(emp_1))
print(emp_1.__str__())
print(str(emp_2))
print(emp_2.__str__())


# for use of __add__() magic method
print(emp_1 + emp_2)

# for use of __len__() magic method
print(len(emp_1))
