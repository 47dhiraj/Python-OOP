class Employee:                                                 # Employee chai parent class ho ..Generally parent class ma sabi subclass lai chaine common code haru lekhincha
    raise_amt = 1.04                                            # Generally class variable is related with class ,,, but some time u can change the value of class variable only for some particular instance or object

    def __init__(self, first, last, pay):                       # __init__ vannale constructor vanne bujincha python ma
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):                                      # Developer chai child or subclass ho
    raise_amt = 1.10                                            # yedi employe ko vanda farak rais_amt sabbai developer lai dina cha vani yesari developer class vitrai class variable banayera raise_amt vale set gare huncha

    def __init__(self, first, last, pay, prog_lang):            # yedi child class ma constructor nai chaina vani, testo condition ma child class le parent class ko constructor lai automatic or by default inherit garcha... yedi child class ma constructor cha vani aafnai class ko constructor use garcha, parent class ko constructor use gardaina
        super().__init__(first, last, pay)                      # super() method le jahile parent class lai bujaucha... # yo line le parent class ko constructor lai call gari rako cha
        # Alternative way of calling constructor of parent class
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang



class Manager(Employee):                                        # Manager chai child or subclass ho

    def __init__(self, first, last, pay, employees=None):       # Manager class ko constructor ho   # yo line ko employees parameter ma employee instance haru aaucha
        super().__init__(first, last, pay)                      # super() method le jahile parent class lai bujaucha... # yo line le parent class ko constructor lai call gari rako cha
        if employees is None:
            self.employees = []
        else:
            self.employees = employees                          # employe instance lai employees vanni list ma haleko

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)                          # emp vannale employee instance lai employees list ma append gareko

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        if not self.employees:
            print(f'\n Currently, no employees are working under Manager. {self.first + self.last}.')
        else:
            print(f'\n Employees working under Manager. {self.first + self.last} are : ')
            for emp in self.employees:
                print('\t\t\t\t\t\t\t\t\t\t -->', emp.fullname())




# print(help(Developer))                  # kunai class ko detail behaviour chyakka sanga herna cha vani help() method ko use garincha
# print(help(Manager))                    # kunai class ko detail behaviour chyakka sanga herna cha vani help() method ko use garincha

dev_1 = Developer('John', 'Doe', 50000, 'Python')                   # creating developer instance
dev_2 = Developer('Jimmy', 'Jimmer', 60000, 'Java')                 # creating another developer instance

if isinstance(dev_1, Developer):
    print('\ndev-1 is the instance of Developer class.')
if isinstance(dev_2, Developer):
    print('dev-2 is the instance of Developer class.')

if isinstance(dev_1, Employee):
    print('\ndev-1 is the also instance of Employee Parent class.')
if isinstance(dev_2, Employee):
    print('dev-2 is the also instance of Employee Parent class.')

if isinstance(dev_1, Manager) == False:
    print('\ndev-1 is not the instance of Manager class.')
if isinstance(dev_2, Manager) == False:
    print('dev-2 is not the instance of Manager class.')



if issubclass(Developer, Employee):
    print('\nDeveloper is the subclass of Parent Employee class')
if issubclass(Manager, Employee):
    print('Manager is the subclass of Parent Employee class')
if issubclass(Developer, Manager) == False:
    print('Developer is not the subclass Manager, rather they are both subclass of Employee parent class \n')


print(dev_1.__dict__)                                               # kunai particular instance sanga related sabbai value haru as a dictionary format ma herna ko lagi  __dict__  ko use garincha
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.__dict__, '\n')                                         # kunai particular instance sanga related sabbai value haru as a dictionary format ma herna ko lagi  __dict__  ko use garincha


print(dev_2.__dict__)
dev_2.apply_raise()
print(dev_2.pay)
print(dev_2.__dict__, '\n')




mgr_1 = Manager('Lord', 'Lingard', 90000)                           # creating manager instance
mgr_1.add_emp(dev_1)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
mgr_1.remove_emp(dev_2)
mgr_1.print_emps()

