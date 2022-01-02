# Example of Inheritance
# kunai auta class ko attributes & methods lai arko class ma use garnu cha vani inheritance ko use garincha

class Dog():
    def __init__(self, name, age):          # constructor of Dog class
        self.name = name
        self.age = age

    def speak(self):
        print('Hi i am ', self.name, ' and i am ', self.age, ' years old.')

    def talk(self):
        print('bark')


class Cat(Dog):             # Dog vanni class lai Cat vanni class le inherit gareko cha (i.e cat is extending from dog class)  # parent class lai inherit garda parent class ko attributes, & methods sabbai inherit huncha child class ma
    def __init__(self, name, age, color):   # constructor of cat class
        super().__init__(name, age)         # constructor inheritance : yedi parent class ko constructor ko code reuse garera attribute lai initialize garnu cha vani yesari garna sakincha
        # self.name = name                  # child class ko constructor ma attribute initialization lai override garna pani sakincha
        # self.age = age                    # child class ko constructor ma attribute initialization lai override garna pani sakincha
        self.color = color                  # # child class ko constructor naya attribute lai initialize gareko

    # Note : hamile Cat class ma Dog class ko speak() method lai nai use gari rako chau

    # Method Overriding case
    def talk(self):         # yedi child ma parent ma same class ko method name having similar signature cha vani, yesto case ma jun class ko object le call gareko cha tei class vitra ko method execute garincha.. yesailai method overriding vanincha
        print('meow')



birali = Cat('birali', 2, 'grey')
puppy = Dog('puppy', 3)

birali.speak()
birali.talk()

puppy.speak()
puppy.talk()
