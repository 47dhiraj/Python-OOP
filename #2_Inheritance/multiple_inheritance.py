class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1
        return self.level


class Employee:
    company = "Visa"
    eCode = 120

    def upgradeLevel(self):
        print('Employee rank is being upgraded')


class Programmer(Freelancer, Employee):
    name = "Rohit"



p = Programmer()

print(p.upgradeLevel())
print(p.company)                # jahile pani multiple inherit garda, yedi upper classes haru ma same naam ko attributes or method cha vani  testo bela ma upper left most class ko attributes & methods le aru upper class ko same naam gareko attributes & methods lai override garcha