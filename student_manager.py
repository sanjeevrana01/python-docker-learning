
import json

student = {
    "name": "Sanjeev",
    "marks": 85,
    "result": "Pass"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Student data saved!")
