#printing objects using __str__....so that we can print data value of any object

class Point:

    def __init__(self,x,y):
        self.x =x
        self.y =y

    def __str__(self):
        result = "X value is {} and Y value is {} ".format(self.x, self.y)
        return result


p = Point(1,2)
print(p)           #object lai print garna khojda automatically pahila  __str__(self) vanni function call hunxa...so,yesari object print garda object vitra ko value print garna skainxa
