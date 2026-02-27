"""
Student Data  Module
Manages Student Data storage (in-memory for now).
"""

#in memory storage
students =[]

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