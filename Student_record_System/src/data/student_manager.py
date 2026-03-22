import json
import os
from src.models.student import Student

FILE_PATH = os.path.join(os.path.dirname(__file__), 'Student.json')

class StudentManager:
    def __init__(self):
        self.student = []

manager = StudentManager()

def load_student(self, filepath = FILE_PATH):
    if os.path.exist(filepath):
        with open(filepath, "r") as f:
            data = json.load(f)
            self.students = (Student.from_dict(d) for d in data)

def save_students(self, filepath = FILE_PATH):
    data = [student.to_dict() for student in self.students]
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def add_student(self, student: Student) -> bool:
    """Add a student, returns False if ID already exists."""
    if self.find_by_id(student.id):
        return False
    self.students.append(student)
    return True


def find_by_id(self, student_id: str) -> Student | None:
    for student in self.students:
        if student.id == student_id:
            return student
    return None

def get_all(self) -> list[Student]:
    return self.students.copy()

def update_student(self, student_id: str, updates: dict) -> bool:
    student = self.find_by_id(student_id)
    if not student:
        return False
    for key, value in updates.items():
        if hasattr(student, key):
            setattr(student, key, value)
    return True

def update_student(self, student_id: str, updates: dict) -> bool:
    student = self.find_by_id(student_id)
    if not student:
        return False
    for key, value in updates.items():
        if hasattr(student, key):
            setattr(student, key, value)
    return True

def delete_student(self, student_id: str) -> bool:
    student = self.find_by_id(student_id)
    if not student:
        return False
    self.students.remove(student)
    return True
