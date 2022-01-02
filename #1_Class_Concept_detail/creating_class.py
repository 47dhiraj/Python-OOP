class Dog():                                       # Dog aauta class ho

    def __init__(self, naam, umer):                # self ma current object aaucha & name vaneko parameter ho # python ma constructor yesari banaincha ... constructor is automatically called when new object is created.. object initialization garna help garcha constructor le... self keyword refers to the current object(instance) of the class which is calling the constructor
        # print(naam)                              # naam chai function ko attribute ho(i.e local attribute)
        # print(umer)                              # umer chai function ko attribute ho(i.e local attribute)
        self.name = naam                           # class ko attribute lai class vitra access garna cha vani self keyword ko use garnu parcha # self.attribute vannale class vitra ko attribute lai janaucha... yedi attribute cha vani class vitra ko attribute lai janaucha, yedi attribute chaina vani class vitra automatic attribute create garcha
        self.age = umer                            # class ko attribute lai class vitra access garna cha vani self keyword ko use garnu parcha # self.attribute vannale class vitra ko attribute lai janaucha... yedi attribute cha vani class vitra ko attribute lai janaucha, yedi attribute chaina vani class vitra automatic attribute create garcha
        # print(self.name)
        # print(self.age)


    # bark() chai dog class ko method ho
    def bark(self):                                # kun instance or object le yo bark() method lai call gareko tha pai rakhna ko lagi self keyword lekhnai parcha... function or definition haru sabbai ma self keyword as signature lekhnai parcha
        print(self.name, 'is barking & his age is ', self.age)

    # change_age() chai dog class ko method ho
    def change_age(self, umer):
        self.age = umer





puppy = Dog('Puppy', 2)                             # yesari new object create garda kheri constructor function call huncha i.e __init__() call huncha
tommy = Dog('Tommy', 3)                             # yesari new object create garda kheri constructor function call huncha i.e __init__() call huncha

print(puppy.age)                                    # Generally, class ko attribute lai object le matra access garna sakcha & access garda self keyword lekhidaina
print(tommy.age)
# Cant do this ==> print(age)                                        # object nai nabanai direct yesari attribute access garna mildaina

puppy.change_age(4)
tommy.change_age(6)

puppy.bark()
tommy.bark()

