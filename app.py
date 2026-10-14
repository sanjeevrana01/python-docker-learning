
import os
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)



def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "db"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        user="root",
        password=os.environ["MYSQL_ROOT_PASSWORD"],
        database="student_db"
    )



@app.route("/")
def home():
    return render_template("index.html", name="Sanjeev Rana")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/hello/<name>")
def hello(name):
    return render_template("index.html", name=name)


@app.route("/students")
def students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, name, email, course FROM students ORDER BY id"
    )
    student_list = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("students.html", students=student_list)


@app.route("/students/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form.get("course") or None

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)",
            (name, email, course)
        )

        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for("students"))

    return render_template("add_student.html")


@app.route("/students/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = %s",
        (student_id,)
    )

    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for("students"))


@app.route("/students/edit/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form.get("course") or None

        cursor.execute(
            "UPDATE students SET name = %s, email = %s, course = %s WHERE id = %s",
            (name, email, course, student_id)
        )

        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for("students"))

    cursor.execute(
        "SELECT id, name, email, course FROM students WHERE id = %s",
        (student_id,)
    )
    student = cursor.fetchone()

    cursor.close()
    connection.close()

    if student is None:
        return "Student not found", 404

    return render_template("edit_student.html", student=student)


@app.route("/students/search", methods=["GET"])
def search_students():
    search_term = request.args.get("q", "").strip()

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT id, name, email, course
        FROM students
        WHERE name LIKE %s OR email LIKE %s
        ORDER BY id
        """,
        (f"%{search_term}%", f"%{search_term}%")
    )

    student_list = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("students.html", students=student_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
