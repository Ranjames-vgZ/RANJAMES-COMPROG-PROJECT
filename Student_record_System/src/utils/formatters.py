"""
formatter Module
Provides formatting function for display output.
"""


def format_student_record(student):
    """
     Format student  record for display.

    Args:
         student (dict) Student dictionary with key: id, name, age, grades,

       Returns
        returns: formatted string
        """
    output = "\n" + "="*60 + "\n"
    output += f"Student ID: {student.id}\n"
    output += f"Name: {student.name}\n"
    output += f"Age: {student.age}\n"

    if student.grades:
        output += f"Grades: {', '.join(map(str, student.grades))}\n"
        if len(student.grades) >= 4:
            weighted_avg = student.grades[0]*0.2 + student.grades[1]*0.2 + student.grades[2]*0.2 + student.grades[3]*0.4
        else:
            weighted_avg = sum(student.grades)/len(student.grades)
        output += f"Average: {weighted_avg:.2f}\n"
    else:
        output += "No grades recorded\n"

    output += "="*60 + "\n"
    return output

def format_table_header():
    """Return formatted table header for student list."""
    header = f"\n{'ID':<12} {'Name':<25} {'Age':<5} {'Avg Grade':<10}\n"
    header += "-"* 52 + "\n"
    return header

def format_table_row(student):
    """Format a single student for table display."""
    student_id = student.id
    name = student.name[:24]
    age = student.age

    if student.grades:
        if len(student.grades) >= 4:
            weighted_avg = student.grades[0]*0.2 + student.grades[1]*0.2 + student.grades[2]*0.2 + student.grades[3]*0.4
        else:
            weighted_avg = sum(student.grades)/len(student.grades)
    else:
        weighted_avg = 0

    return f"{student_id:<12} {name:<25} {age:<5} {weighted_avg:<10.2f}\n"