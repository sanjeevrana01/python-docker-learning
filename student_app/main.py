
from student import Student
from storage import load_students, save_students


students = load_students()

while True:
    print("\n--- Student Management ---")
    print("1. Add student")
    print("2. View students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Student name: ")

        try:
            marks = int(input("Marks (0-100): "))
            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                continue
        except ValueError:
            print("Please enter a whole number.")
            continue

        students.append({
            "name": name,
            "marks": marks
        })
        save_students(students)
        print("Student saved!")

    elif choice == "2":
        for record in students:
            student = Student(
                record["name"], record["marks"]
            )
            student.display()
            print("----------")

        if not students:
            print("No students found.")

    elif choice == "3":
        break

    else:
        print("Invalid option.")
