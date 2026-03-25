"""
Student Data  Module
Manages Student Data storage (in-memory for now).
"""
import json
import os


FILE_PATH = os.path.join(os.path.dirname(__file__), 'Student.json')

# In memory student storage
students = []

def load_students(filepath=FILE_PATH):
    """
    Load student records from a JSON file.
    """
    global students
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                students = json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading students from file: {e}")
        students = []

def save_students(filepath=FILE_PATH, students_data=None):
    """
    Save student records to a JSON file.
    """
    if students_data is None:
        students_data = students
    
    try:
        with open(filepath, 'w') as file:
            json.dump(students_data, file, indent=4)    
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error saving students to file: {e}")


def add_student(student):
    """
    Add a student to the database.

    Args:
        student (dict): Student Dictionary

    Returns:
        bool: True if added succesfully
    """
# Checks  for duplicates ID
    if find_student_by_id(student['id']):
        return False
    
    students.append(student)
    return True

def find_student_by_id(student_id):
    """
    Find student b ID,

    Args:
        student_id(str): Student ID to serarch

    Returns:
        dict or None: Student dictionary if found, None Otherwise
    """
    for student in students:
        if student['id'] == student_id:
            return student
    return None

def get_all_students():
    """Return List of all students."""
    return students.copy()

def update_student(student_id, updated_data):
    """
    Update student information.

    Args:
        student_id(str): Student ID
        updated_Data (dict): Dictionary with fields to update

    Returns:
        bool: True if Updated successfully
    """
    student = find_student_by_id(student_id)
    if not student:
        return False
    
    student.update(updated_data)
    return True

def delete_student(student_id):
    """
    Delete a student.

    Agrs:
        student_id (str): Student ID

    Returns:
        Bool: true if deleted successfully
    """
    student = find_student_by_id(student_id)
    if not student:
        return False
    
    students.remove(student)
    return True

def get_student_count():
    """Return total number of students."""
    return len(students)
