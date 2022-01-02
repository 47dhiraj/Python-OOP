# calling parent's constructor with parameters
class Employee:   
    def __init__(self, salary):  
        self.salary = salary
        self.position = "employee"
        self.department = "Account"

    
class BankEmployee(Employee):
    def __init__(self, name, sal):
        super().__init__(sal)
        self.name = name
    

emp = BankEmployee("Ram", 2000)
print(type(emp))

print(emp.name)
print(emp.salary)
print(emp.position)
print(emp.department)

