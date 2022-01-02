# One way ==> You can create object of inner class inside the outer class
# OR
# 2nd way ==> You can also create object of inner class outside the outer class provide if you use outer class name to call it

class Student:                          # Student chai outer class jastai ho
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()        # creating object of inner class(i.e Laptop) inside the outer class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()                 # calling method of inner class

    class Laptop:                       # Laptop chai inner class jastai ho yaha
        def __init__(self):
            self.brand = "Hp"
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)



s1 = Student('Timmy', 1)
s2 = Student('Jimmy', 2)
s1.show()
s2.show()


# lap1 = Student.Laptop()                 # creating object of inner class outside the outer class
# lap1 = s1.lap
# lap2 = s2.lap
# print(id(lap1))
# print(id(lap2))