#Adiing methods

class Point:
    def __int__ (self, x, y):
        self.x = x
        self.y = y
    
    def substract(self):
        result = self.x - self.y
        return result
    
p = Point(1,2)        
q = Point(3,4)

print(p.x,p.y)
print(q.x,q.y)

p_result = p.substract()
q_result = q.substract()

print(p_result)
print(q_result)