#method overriding garda, priority chai child class ko method lai dinxa,,, & incase child class ma method vetena vani balla Parent class ko method lai priority dinxa

'''
#method overriding


class Animal:
    def speak(self):
        print("Speaking")

class Dog(Animal):
    def speak(self):                #yo function chai call hunxa
        print("barking")

d =Dog()           #creating Dog(child) class object
d.speak()          #calling child class speak() function ...i.e here it is overriding parent class speak() functio

'''


'''
#without method overriding

class Animal:
    def speak(self):
        print("Speaking")

class Dog(Animal):
    pass
    
    
d =Dog()          
d.speak()   #yo sepak() function chai Dog class ma xaina i.e dog class le override garena.... so finaaly yo function lai khojdai parent(Animal) class ma janxa   

'''