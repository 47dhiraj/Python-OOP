class Employee:
    company = "Reksha Company"
    salary = 5600
    salarybonus = 400

    @property                                   # @property matra cha vani Getter vayo
    def totalSalary(self):                      # auta yesto function jun property or attribute jasari kaam garcha... so yesto function banauna function mathi @property lekhna parcha
        return self.salary + self.salarybonus

    @totalSalary.setter                         # @property.setter garyo vani kunai property ko value lai set pani garna sakincha
    def totalSalary(self, val):
        self.salarybonus = val - self.salary


e = Employee()                              # creating new object
print(e.totalSalary)                        # totalSalary ahile property jasto vai sakyo so call garda kheri () lekhna pardaina

e.totalSalary = 5800                        # yo line le totalSalary(self, val) lai call garcha i.e setter ho yo

print(e.company)
print(e.salary)
print(e.salarybonus)