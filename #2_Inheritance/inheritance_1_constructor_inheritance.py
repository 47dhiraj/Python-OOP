class Pet:                                      # Pet chai Parent(super) class ho
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} & i am {self.age} years old.")

    def speak(self):
        print("I don't speak.")




# Note : super() references to the parent class ... super().method()   garera parent class ko method lai pani call garna sakincha ... for eg: super().__init__()

class Dog(Pet):                                 # Dog is child class inheriting from Pet class
    def __init__(self, name, age, color):
        super().__init__(name, age)             # CONSTRUCTOR INHERITANCE  : yo line le constructor inheritance gari rako cha (i.e code reusability vayo.. same code repeated way ma lekhna parena)
        # Alternative code for constructor inheritance
        # self.name = name
        # self.age = age
        self.color = color

    def show(self):
        print(f"I am {self.name} & i am {self.age} years old & i looks {self.color}.")

    def speak(self):
        print("Bark")

class Cat(Pet):                                 # Cat is child class inheriting from Pet class
    def speak(self):
        print("Meow")

class Fish(Pet):                                # Fish is child class inheriting from Pet class
    pass


p = Pet("Tim", 20)
p.show()
p.speak()

d = Dog("puppy", 5, "grey")
d.show()
d.speak()

c = Cat("birli", 5)
c.show()
c.speak()

f = Fish("macha", 5)
f.show()
f.speak()






