#Multiple Inheritance

class Animal:
    def speak(self):
        print("Animal speaking")

class Dog:
    def bark(self):
        print("Dog Barking")

#The child class Tommy inherits class Dog and Animal

class Tommy(Animal, Dog):     #Tommy (child) class is inherting from both Animal & Dog (parent classes)
    def eat(self):
        print("Tommy eating brad....")

d = Tommy()
d.eat()
d.bark()
d.speak()


#issubclass
print(issubclass(Tommy, Dog))
print(issubclass(Tommy, Animal))
print(issubclass(Dog, Animal))

#isinstance
t = Tommy()
d = Dog()
print(isinstance(t, Tommy))       #aafno object aafno lagi tw vai nai halxa
print(isinstance(t, Dog))         #child(Tommy) ko object, parent(Dog)  ko pani object hunxa
print(isinstance(t, Animal))      #child(Tommy) ko object, parent(Animal) ko pani object hunxa
print(isinstance(d, Animal))      #arkai class(Dog) ko object, kunai arkai class(Animal) ko object hunai sakdaina

a = Animal()
print(isinstance(a, Tommy))       #parent(Animal) ko object, child(Tommy) ko pani object hunai sakdaina



