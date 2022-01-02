class Student:

    def read_marks(self):
        self.marks=0
        for i in range(8):
            mark = int(input("Enter mark of subject {}".format(i+1)))
            self.marks = self.marks + mark

    def calculate_division(self):
        percentage = (self.marks/800.0)*100;
        if percentage >=80:
            self.division = "Distinction"
        elif percentage >=60:
            self.division = "First Division"
        elif percentage >=40:
            self.division = "Second Division"
        else:
            self.division = "Fail"

    def show_division(self):
        print("Division: " + self.division)

student1 = Student()
student1.read_marks()
student1.calculate_division()
student1.show_division()