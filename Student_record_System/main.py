# """
# Student Record Management System
# Main Program  


# Author(s): [Ranjames P. Anuario] 
# Date: [02/02/2026] 
# Version: 1.0 Part - 1 
# """

# from src.models.student import Student
# from src.data.student_manager import StudentManager
# from src.utils import helpers, validators, formatters


# def display_menu():
#     """Display main menu."""
#     print("\n" + "="*60)
#     print("STUDENT RECORD MANAGEMENT SYSTEM")
#     print("-"*60)
#     print("1. Add Student")
#     print("2. View All Students")
#     print("3. Search Student")
#     print("4. Update Student")
#     print("5. Delete Student")
#     print("6. Exit")
#     print("-"*60)

# def add_student_menu(manager: StudentManager):
#     """Add new student"""
#     print ("\n" + "="*60)
#     print("ADD NEW STUDENT")
#     print("="*60)

#     #Get student ID
#     student_id = helpers.get_valid_input(
#         "Enter Student ID (YYYY-SS-NNNN): ",
#         validators.validate_student_id,
#         "Invalid Id Format! Use YYYY-SS-NNNN"
#     )

#     #Checks if Id Exists
#     if manager.find_by_id(student_id):
#         print(f"Student ID{student_id} Already Exist!")
#         helpers.pause()
#         return
    
#     #Get student name
#     name = helpers.get_valid_input( 
#         "Enter Name: ",
#         validators.validate_name, 
#         "Invalid name! Must be at least 2 characters" 
#         ).title() 
    
#     #Get student age 
#     age = int (helpers.get_valid_input( 
#          "Enter Age: ", 
#          validators.validate_age, 
#          "Invalid age! Must be between 17-100"
#     ))  

#      #Get email
#     email = helpers.get_valid_input( 
#         "Enter Email: ", 
#         validators.validate_email, 
#         "Invalid email format!" 
#     ).lower() 
    
#     #Create student record 
#     student = Student(student_id, name, age, email, grades=[])
#     #Add to Database
#     if manager.add_student(student):
#         print(f"\nStudent {name} added Successfully")
#         manager.save_students()
#     else:
#         print("\nFailed to add student!")
    
#     helpers.pause()

# def view_all_students(manager): 
#         """Display all students.""" 
#         print("\n" + "="*60) 
#         print("ALL STUDENTS") 
#         print("-"*60) 
        
#         students = manager.get_all()
        
#         if not students: 
#             print("No students in the system.") 
#         else: 
#             print(formatters.format_table_header(), end="")
#             for student in students:    
#                print(formatters.format_table_row(student), end="") 
            
#         helpers.pause()
        
# def search_student(manager):
#         """Search for a student by ID."""
#         print("\n" +"="*60) 
#         print("SEARCH STUDENT") 
#         print("-"*60) 

#         student_id = helpers.get_valid_input(
#         "Enter Student ID: ",
#         validators.validate_student_id,
#         "Invalid ID format! Use YYYY-SS-NNNN"
#         )  
        
#         student = manager.find_by_id(student_id) 
        
#         if student:
#             print(formatters.format_student_record(student))  
#         else: 
#             print(f"Student ID {student_id} not found!")
        
#         helpers.pause()

# def update_student_menu(manager): 
#     """Update student information.""" 
#     print("\n" + "="*60) 
#     print("UPDATE STUDENT") 
#     print("-"*60) 
    
#     student_id = helpers.get_valid_input(
#     "Enter Student ID: ",
#     validators.validate_student_id,
#     "Invalid ID format! Use YYYY-SS-NNNN"
#     )
        
#     student = manager.find_by_id(student_id) 
    
#     if not student: 
#         print (f"Student ID {student_id} not found!") 
#         helpers.pause() 
#         return 
    
#     print(f"\nCurrent information:") 
#     print(formatters.format_student_record(student)) 
   
#     print("\nwhat would you like to update?") 
#     print("1. Name") 
#     print("2. Age") 
#     print("3. Email") 
#     print("4. Cancel") 
    
#     choice = input("Choice: ").strip() 
    
#     updated_data = {}

#     if choice == "1": 
#         name = helpers.get_valid_input( 
#             "New Name:",
#             validators.validate_name, 
#             "Invalid name!" 
#             ).title() 
#         updated_data['name'] = name 

#     elif choice == "2": 
#         age = int (helpers.get_valid_input(
#             "New Age: ",
#             validators.validate_age, 
#             "Invalid age!"
#             ))
#         updated_data['age'] = age 

#     elif choice == "3": 
#         email = helpers.get_valid_input( 
#             "New Email: ", 
#             validators.validate_email, 
#             "Invalid email!" 
#             ).lower() 
#         updated_data['email'] = email 
        
#     elif choice == "4": 
#         print("Update cancelled.") 
#         helpers.pause() 
#         return 
    
#     else: 
#         print("Invalid choice!") 
#         helpers.pause() 
#         return 
    
#     if manager.update_student (student_id, updated_data): 
#         print("\nStudent updated successfully!") 
#         manager.save_students()
#     else: print("\nFailed to update student!") 
    
#     helpers.pause()

# def delete_student_menu(manager): 
#     """Delete a student.""" 
#     print("\n" + "="*60) 
#     print("DELETE STUDENT") 
#     print("-"*60) 
    
#     student_id = helpers.get_valid_input(
#         "Enter Student ID: ",
#         validators.validate_student_id,
#         "Invalid ID format! Use YYYY-SS-NNNN"
#         )  

#     student = manager.find_by_id(student_id) 
#     if not student: 
#         print (f"Student ID {student_id} not found!") 
#         helpers.pause() 
#         return 
    
#     print(f"\nStudent to delete:") 
#     print(formatters.format_student_record(student))

#     confirm = input("Confirm deletion? (yes/no): ").strip().lower() 
    
#     if confirm == "yes": 
#         if manager.delete_student(student_id): 
#             print("\nStudent deleted successfully!")
#             manager.save_students()
#         else: 
#             print("\nFailed to delete student!") 
#     else: 
#         print("Deletion cancelled.") 
        
#         helpers.pause()
   
# def main():
#     """Main program loop."""
#     print("\n" + "="*60)
#     print("Welcome to Student Record Management System")
#     print("Version 1.0 Part 1: Refactored with OOP")
#     print("-"*60)

#     manager = StudentManager()
#     manager.load_students()

#     helpers.pause()

#     while True:
#         display_menu()
#         choice = input("Enter choice (1-6): ").strip()

#         if choice == "1":
#             add_student_menu(manager)
#         elif choice == "2":
#             view_all_students(manager)
#         elif choice == "3":
#             search_student(manager)
#         elif choice == "4":
#             update_student_menu(manager)
#         elif choice == "5":
#             delete_student_menu(manager)
#         elif choice == "6":
#             print("\nThank you for using Student Record Management System! GOODBYE!")
#             break







#         else:
#             print("\nInvalid choice!")
#             helpers.pause()

# if __name__ == "__main__":
#     main()

from src.ui.main_window import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()