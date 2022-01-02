# Example of working with multiple related class... auta class ko object arko class vitra use garne kura sikchau

class Student:                                     # Student vanni class
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []                          # Course class and Student class lai link garaune kaam yo students vanni list le gari rako cha... jati pani students object haru banchan tyo sabbai students lai yo students vanni list ma rakhincha

    def add_student(self, student):                 # yo line ko student vanni parameter ma naya add garne auta student object aaucha
        if len(self.students) < self.max_students:
            self.students.append(student)           # studnets vanni list ma auta student object lai append gareko


    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()            # particular course ko lagi sabbai students haru lai herera average grade nikalne logic ho yo

        return value/len(self.students)


s1 = Student("John", 24, 80)
s2 = Student("Doe", 24, 70)
s3 = Student("David", 24, 60)
s4 = Student("Michael", 24, 75)
s5 = Student("Jimmy", 24, 85)
s6 = Student("Timmy", 24, 90)




course1 = Course('Science', 2)                       # yo line ko 2 vannale, science course ma maximum no. of student chai 2 vaneko
course1.add_student(s1)
print(course1.students[0].name)                     # auta class ko object le arko class ko object lai call garda bich ma . operator use garna parcha
course1.add_student(s2)
print(course1.students[1].name)
print(course1.get_average_grade())

course1.add_student(s3)                              # autai course ma 2 ta vanda badi student add garna mildaina
print(course1.get_average_grade())                   # since 2 ta vanda badi student add garna namile pachi average grade pani same nai rahancha





course2 = Course('Math', 3)                          # yo line ko 3 vananle, Math course ma maximum no. of student chai 3 vaneko
course2.add_student(s3)
print(course2.students[0].name)                     # auta class ko object le arko class ko object lai call garda bich ma . operator use garna parcha
course2.add_student(s4)
print(course2.students[1].name)
course2.add_student(s5)
print(course2.students[2].name)
print(course2.get_average_grade())

course2.add_student(s6)                             # Math vanni course ma 3 ta student vanda badi student add garna mildaina
print(course2.get_average_grade())                  # 3 ta vanda badi student add garna namile pachi average_grade pani same nai rahancha





