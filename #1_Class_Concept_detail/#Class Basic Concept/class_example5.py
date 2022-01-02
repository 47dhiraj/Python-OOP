#objects aliasing

def modify(obj):
    obj.x = 5            #user define objects are mutable i.e change garna milne (i.e yaha object obj ko x ko value ma 5 halda p object ko x ko value pani 5 hunxa)

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

p= Point(1,2)

modify(p)

print(p.x,p.y)