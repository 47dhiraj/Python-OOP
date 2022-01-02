class Pet:                          # Pet chai Parent(super) class ho
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} & i am {self.age} years old.")

    def speak(self):
        print("I don't speak.")



class Dog(Pet):                     # Dog is child class inheriting from Pet class ... yeti bela chai parent class ma vayeko sabbai methods haru chai inherit huncha but parent class ko constructor vitra ko attribute haru chai inherit hudaina... constructor lai pani inherit garna ko laig constructor inheritance garna parcha
    def speak(self):                # Method Overriding : yo speak() method le pet(parent) class ko speak() method lai override garcha
        print("Bark")

class Cat(Pet):                     # Cat is child class inheriting from Pet class
    def speak(self):                # Method Overriding : yo speak() method le pet(parent) class ko speak() method lai override garcha
        print("Meow")

class Fish(Pet):                    # Fish is child class inheriting from Pet class
    pass


p = Pet("Tim", 20)
p.show()
p.speak()

d = Dog("puppy", 5)
d.show()
d.speak()


c = Cat("birli", 5)
c.show()
c.speak()

f = Fish("macha", 5)
f.show()
f.speak()

