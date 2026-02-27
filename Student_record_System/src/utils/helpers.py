"""
Helpers Module
Provides helper function for commmon task.
"""

def get_valid_input(prompt, validation_func, error_msg = "Invalid input!"):
    """
    Get validdate input from user.
    
    Args:
        prompt (str): Input prompt
        validation_func (funtion): Function to validate input
        error_msg (str): Error message for invalid input

    Returns:
        str: Valid user input
    """
    while True:
        user_input  = input(prompt).strip()
        if validation_func(user_input):
            return user_input
        print(f"{error_msg}")

def pause():
        """Pause and wait for user to press Enter"""
        input("\nPress Enter to cotinue...")

def clear_screen():
        """Clear the console screen"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

def generate_student_id(start_year, semester, number):
        """
        Generate student ID in Format YYYY-SS-NNNN.

        Agrs:
            start_year(int): Starting year of academic year (e.g., 2025 for 2025-2026)
            semester (int): Semester number (e.g., 1 for first semeter)
            number(int): Student enrollee nbumber
        
        Returns:
            str: Formatted student ID

        Example:
            >>>>generate_student_id(2025, 1 1234)
            '2526-02-1234'
            >>>>generate_student_id(2024, 2, 5)
            '2425-02-0005'  
        """
        #combine Last two digits of academic year
        year1 = start_year % 100
        year2 =(start_year+1) % 100
        year_part = f"{year1:02d}{year2:02d}"

        # Format semester as 2 digits 
        semester_part = str(semester).zfills(2)

        #fromat semester as 4 digits
        number_part = str(semester).zfills(4)

        return f"{year_part}-{semester_part}-{number_part}"
    