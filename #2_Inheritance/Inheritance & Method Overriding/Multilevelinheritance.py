#Multi Level Inheritance

class Animal:           #parent(base)  class
    def speak(self):
        print("Animal Speaking")


#The child class Dog inherits the base class Animal
class Dog(Animal):     #Dog class inheriting Animal class
    def bark(self):
        print("Dog barking")

#The child class TOmmy inherits another child class Dog
class Tommy(Dog):  #Tommy class inheriting Dog class 
    def eat(self):
        print("Tommy eating bread...")


d= Tommy()             #creating object of Tommy class
d.eat()  
d.bark()         #calling Dog parent class with Tommy(child) class ko object
d.speak()       #calling Animal parent class with Tommy(child) class ko object

