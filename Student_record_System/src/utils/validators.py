"""
Validators Module
Provides validation function for  student data
"""

def validate_student_id(student_id):
    """
    Validate student ID format: YYY-SS_NNNN
    
    Args:
        student_id(str): Student ID to validate 
    
    ReturnS:
        bool: True if valid, False otherwise
        
    Example:
        >>> validate_student_id("2526-01-1234")
        True
        >>> validate_student_id("2024-0001")
        False
        >>> validate_student_id("2526-01-1234")
        False
    """
    if not isinstance(student_id, str):
        return False
    
    parts = student_id.split('-')
    if len(parts) != 3:
        return False

    year, semester, number = parts
    
    #validate year must ve 4 digits
    if len(year) != 4 or not year.isdigit():
        return False
    
    #validate semester: must be 2 digits
    if len(semester) !=2 or not semester.isdigit():
        return False
    
    #validate number: must be 4 digits
    if len(number) != 4 or not number.isdigit():
        return False

    return True

def validate_name(name):
    """Validate student name."""
    if not name or not isinstance(name, str):
        return False
    name = name.strip()
    if len(name) < 2:
        return False
    return all(c.isalpha() or c.isspace() for c in name)

def validate_age(age):
    """Validate student age."""
    try:
        age = int(age)
        return 17 <= age <=100
    except (ValueError, TypeError):
        return False
    
def validate_grade(grade):
    """Validate grade (60-100)."""
    try:
        grade = float(grade)
        return 60 <= grade <=100
    except (ValueError, TypeError):
        return False
    
def validate_email(email):
    """
    Basic email Validation.
    
    Rules:
    -Must have exactly one "@" symbol.
    -Must  have username before @
    -Must have a domain with atleast one dot after @
    -cannot 
    -Domain name must have at least one "." character.
    """
    if not email or not isinstance(email, str):
        return False
    
    email = email.strip().lower()

# Check for spaces
    if ' ' in email:
        return False

#Must have exactly one @ symbol
    if email.count('@') != 1:
        return False

#split by @
    parts = email.split('@')
    username, domain = parts[0],parts[1]

#Username must not be empty
    if not username:
        return False

#domain must have atleast one dot
    if '.' not in domain:
        return False
    
#domain must have content after the last dot
    domain_parts = domain.split('.')
    if not domain_parts[-1]:
        return False

    return True 