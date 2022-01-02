#calling parents constructor with parameters

class employee:
    def __init__(self, salary):
        self.salary = salary

class bankemployee(employee):
    def __init__(self, name, salary):
        super().__init__(salary)                # yo just code reusability ko kaam gari rako cha
        self.name = name


emp = bankemployee("ram", 2000)
print(emp.name)
print(emp.salary)