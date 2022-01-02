'''
#without Method resoultion order(By Default ordering)

class A:
    def test(self, param):
        print("test of A")

class B:
    def test(self, param):
        print("test of B")

class Shape(B,A):   #By default method resoluiton order Shape() ko bracket ma B pahila xa then A xa, So B ko test method call hunxa  
    pass


shape = Shape()  #shape vanni object banako Shape class ko
shape.test(4)
'''


'''

#Method resolution order
class A:
    def test(self, param):
        print("test of A")

class B:
    def test(self, param):
        print("test of B")

class Shape(B,A):      #At first, Shape class mai test method xa ki vanera check garxa .. But paudaina,, then  B ko test method call hunxa ,,,,in case test method napako vaye A ko test method call hunxa
    pass


shape = Shape()  #shape vanni object banako Shape class ko
shape.test(4)
print(Shape.__mro__)         #__mro__ vaneko method resolution order ho...jasle kunai 2 ta class ma same function cha vani..kun function lai pahila call garne vanera priorty order maintain garxa


'''