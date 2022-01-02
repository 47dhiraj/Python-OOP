#passing parameters to constructor

class Point:                             

    def __init__(self, a, b):       
        self.x = a
        self.y =b

 

                                          
p = Point(1,2)        
q = Point(3,4)



print(p.x) 
print(p.y)
print(q.x)
print(q.y)
