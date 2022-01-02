class Dog:
    total_dogs = []
    def __init__(self, nickname, name):               # constructor vitra ko variable sanga matra particular object ko sarokar huni ho
        self.nickname = nickname
        self.name = name
        self.total_dogs.append(self.name)

    @classmethod
    def num_dogs(cls):                         # classmethod haru kunai particular object sanga related hudaina yo tw class sanga related huni method ho # classmethod haru lai pani instance nabanai siddai classname.method() garera call garna sakincha.. # arko main kura vaneko yo method vitra chai class ko just vitra ko open attribute lai access garna sakincha using  cls  keyword
        return (cls.total_dogs)                # cls keyword ko help batw class ko just vitra ko attribute lai access gareko



pup = Dog(['kutte 1, kamine 1, wafadar 1'], "puppy")                # creating pup object
tim = Dog(['kutte 2, kamine 2, wafadar 2'], "timmy")                # creating tim object


print('Name : ', pup.name, ' Nickname : ', pup.nickname)
print('Name : ', tim.name, ' Nickname : ', tim.nickname)


print(Dog.num_dogs())                              # syntax of calling classmethod ==> classname.method()
