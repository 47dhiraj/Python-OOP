#data abstraction in python
#public memebers can be accessed outsdie of the class using its objects ,,,,,& also child class banayera pani tyo child class vitra acces garna sajilari pai halxa

class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.salary = sal

e1 = Employee("Ram", 2000)

print(e1.name)
print(e1.salary)

