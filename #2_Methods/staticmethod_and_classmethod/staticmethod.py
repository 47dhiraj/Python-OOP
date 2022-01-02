class Dog:
    dogs = []                               # class vitra ko variable

    def __init__(self, name):               # constructor
        self.name = name
        self.dogs.append(self)


    @staticmethod                           # yo line ko @staticmethod chai auta decorator ho
    def bark(n):                            # yedi kunai function lai object or instance nabanai just class ko naam batw call garna cha vani teti bela staticmethod banauni ...  yedi kunai function ma constructor ma vayeko attribute ko value or class ko attribute haru lai access garna kahilai jarurat nai pardaina vani testo bela kunai function lai staticmethod banauni
        for _ in range(n):
            print('Bark !')


Dog.bark(5)                 # syntax of calling staticmethod ==> classname.method(parameter)
