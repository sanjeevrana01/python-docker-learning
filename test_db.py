
import os
import mysql.connector

connection = mysql.connector.connect(
    host="db",
    user="root",
    password=os.environ["MYSQL_ROOT_PASSWORD"],
    database="student_db"
)

print("Connected to MySQL successfully!")

cursor = connection.cursor()
cursor.execute("SELECT id, name, email, course FROM students")

for student in cursor.fetchall():
    print(student)

cursor.close()
connection.close()
