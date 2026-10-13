
import json
import os

FILE_NAME = os.path.join(
    os.path.dirname(__file__), "students.json"
)


def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)
