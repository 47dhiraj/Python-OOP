class Dog:
    # total_dogs = []                               # class vitra ko variable jun sanga particular object ko kei sarokar hudaina... yes sanga class ko sarokar huncha

    def __init__(self, nickname, name):               # constructor vitra ko variable sanga matra particular object ko sarokar huni ho
        self.nickname = nickname
        self.name = name
        # self.total_dogs.append(self.name)              # since total_dogs vanni list constructor vanda bahira declar gareko cha,, this list is not assosciated with any particular object... we can say that this list is only concerned only with Dog class # jun sukai object ko name chai dogs vanni class ko attribute ma gayera append vayera bascha


pup = Dog(['kutte 1, kamine 1, wafadar 1'], "puppy")                # creating pup object
tim = Dog(['kutte 2, kamine 2, wafadar 2'], "timmy")                # creating tim object


print('Name : ', pup.name, ' Nickname : ', pup.nickname)
print('Name : ', tim.name, ' Nickname : ', tim.nickname)



# print(Dog.total_dogs)                                   # sabbai object batw add vayeko dogs haru lai yesari global class variable ma rakhincha which can be easily accessible from anywhere
