"""
Docstring for Student_record_System.src.data.student_manager
"""
# import json
import sqlite3
import os
from src.models.student import Student

# FILE_PATH = os.path.join(os.path.dirname(__file__), 'Student.json')
DB_PATH = os.path.join(os.path.dirname(__file__), 'students.db')

class StudentManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()
        self.create_table()

    
    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL
        )
        """)
        self.conn.commit()

    # def load_students(self, filepath=FILE_PATH):
    #     if os.path.exists(filepath):
    #         with open(filepath, "r") as f:
    #             data = json.load(f)
    #             self.students = [Student.from_dict(d) for d in data]

    # def save_students(self, filepath=FILE_PATH):
    #     """Save students to JSON file."""
    #     data = [student.to_dict() for student in self.students]
    #     with open(filepath, 'w') as f:
    #         json.dump(data, f, indent=4)

    def add_student(self, student: Student) -> bool:
        if self.find_by_id(student.id):
            return False

        self.cursor.execute("""
        INSERT INTO students (id, name, age, email)
        VALUES (?, ?, ?, ?)
        """, (student.id, student.name, student.age, student.email))

        self.conn.commit()
        return True

    def find_by_id(self, student_id: str):
        self.cursor.execute("""
        SELECT * FROM students
        WHERE id = ?
        """, (student_id,))

        data = self.cursor.fetchone()

        if data:
            return Student(
                student_id=data[0],
                name=data[1],
                age=data[2],
                email=data[3]
            )

        return None

    def get_all(self):
        self.cursor.execute("SELECT * FROM students")

        rows = self.cursor.fetchall()

        students = []

        for data in rows:
            student = Student(
                student_id=data[0],
                name=data[1],
                age=data[2],
                email=data[3]
            )
            students.append(student)

        return students

    def count(self):
        self.cursor.execute("SELECT COUNT(*) FROM students")
        return self.cursor.fetchone()[0]

    def update_student(self, student_id: str, updates: dict) -> bool:
        student = self.find_by_id(student_id)

        if not student:
            return False

        if "name" in updates:
            self.cursor.execute("""
            UPDATE students
            SET name = ?
            WHERE id = ?
            """, (updates["name"], student_id))

        if "age" in updates:
            self.cursor.execute("""
            UPDATE students
            SET age = ?
            WHERE id = ?
            """, (updates["age"], student_id))

        if "email" in updates:
            self.cursor.execute("""
            UPDATE students
            SET email = ?
            WHERE id = ?
            """, (updates["email"], student_id))

        self.conn.commit()
        return True

    def delete_student(self, student_id: str) -> bool:
        student = self.find_by_id(student_id)

        if not student:
            return False

        self.cursor.execute("""
        DELETE FROM students
        WHERE id = ?
        """, (student_id,))

        self.conn.commit()
        return True