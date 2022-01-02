# Note : Magic or Dunder methods are python inbuilt methods,, they are denoted by __name__() & they gets called when u do certain operation to the objects ... you can override these methods for your needs

class Point():
    def __init__(self, x=0, y=0):                       # python ma constructor yesari banaincha
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)



    # Inbuilt magic method for addition of the objects
    def __add__(self, p):                               # object + object garyo vani chai yo __add__() magic method call huncha i.e objects ma + operation garyo vani yo magi method call huncha
        return Point(self.x + p.x, self.y + p.y)        # returning the point object

    def __sub__(self, p):                               # object - object garyo vani chai yo __sub__() magic method call huncha
        return Point(self.x - p.x, self.y - p.y)        # returning the point object

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y              # This time we are returnint the value after multipication.. point object pani return garna sakincha but this time we want to return value




    # # Comparing using own created length() method
    # def length(self):
    #     import math
    #     return math.sqrt(self.x**2 + self.y**2)
    #
    # def __gt__(self, p):
    #     return self.length() > p.length()
    #
    # def __ge__(self, p):
    #     return self.length() >= p.length()
    #
    # def __lt__(self, p):
    #     return self.length() < p.length()
    #
    # def __le__(self, p):
    #     return self.length() <= p.length()




    # # Comparing using __len__() magic method
    def __len__(self):
        import math
        return math.ceil(math.sqrt(self.x ** 2 + self.y ** 2))

    def __gt__(self, p):
        return len(self) > len(p)

    def __gt__(self, p):
        return len(self) >= len(p)

    def __lt__(self, p):
        return len(self) < len(p)

    def __le__(self, p):
        return len(self) <= len(p)






    def __eq__(self, p):
        return self.x == p.x and self.y == p.y


    def __str__(self):                                  # __str__() magic method chai object lai print garda automatically call huncha
        return '(' + str(self.x) + ',' + str(self.y) + ')'  # string value return garna parcha


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)


# Calling the Magic methods using respective operation on the objects
p5 = p1 + p2
p6 = p4 - p1
p7 = p2 * p3

# print(p1 == p2)

# Comparing objects
print(p1 > p2)
print(p1 >= p2)
print(p1 < p2)
print(p1 <= p2)




print(p5, p6, p7)           # yesari object lai print(object) garda __str__() method method call huncha






