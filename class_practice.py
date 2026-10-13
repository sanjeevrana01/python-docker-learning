
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        if self.marks >= 50:
            return "Pass"
        else:
            return "Fail"


student1 = Student("Sanjeev", 85)
student2 = Student("Priya", 42)

print(student1.name, student1.check_result())
print(student2.name, student2.check_result())
