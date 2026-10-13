
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        return "Pass" if self.marks >= 50 else "Fail"

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Result: {self.check_result()}")
