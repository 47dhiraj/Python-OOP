#creation of classes

class Point:                  #class banauda class ko name huna paryo & convention Firstletter capital

    def __init__(self):       #__init__ chai python ko inbuilt constructor ho and yo function jasto hunxa.... jaslai jahile suru ma self vanni parameter receive garxa
        self.x = 0
        self.y =0

 
# p & q are objects
                                          
p = Point()        #Point() vanni class ko name ho but it automatically call __init__ constructor at the time of object creation ho
q = Point()


#Accessing object's properties
#Each object has its own x and y
print(p.x) 
print(p.y)
print(q.x)
print(q.y)
