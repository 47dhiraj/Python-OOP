#objects copying

import copy
class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point(1,2)
q = copy.copy(p)
q.x = 2

print(p == q)
print(p is q)   #is le memory refrence check garxa
print(p.x)
print(q.x)
