#Non callable object

class Test1:
    def __init__(self,a):
        self.a = a
    
    def __call__(self):               # python inbuilt __call__() callable method ko kaam vaneko kunai instance or object lai as a method jasari call garna sakne banaunu ho
        print("You have called an object")

t1 = Test1(12)          # creating new object
t1()                    # yo chai object lai call gareko as a method.. (i.e method lai call gare jasari object lai call gari rako cha)
