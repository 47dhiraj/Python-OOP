class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

    # Alternative without creating classmethod
    # def changeSalary(self, sal):
    #     self.__class__.salary = sal



e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)

