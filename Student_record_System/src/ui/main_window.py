import customtkinter as ctk
from src.data.student_manager import StudentManager
from src.models.student import Student
from src.utils.validators import validate_student_id, validate_name, validate_age


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Student Record System")
        self.geometry("750x550")
        self.configure(fg_color="Black")

        self.manager = StudentManager()

        self.id_entry = ctk.CTkEntry(self, placeholder_text="Student ID")
        self.id_entry.pack(pady=5)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Name")
        self.name_entry.pack(pady=5)

        self.age_entry = ctk.CTkEntry(self, placeholder_text="Age")
        self.age_entry.pack(pady=5)


        ctk.CTkButton(self, text="Add Student", command=self.add_student).pack(pady=5)
        ctk.CTkButton(self, text="View Students", command=self.view_students).pack(pady=5)
        ctk.CTkButton(self, text="Search Student", command=self.search_student).pack(pady=5)
        ctk.CTkButton(self, text="Delete Student", command=self.delete_student).pack(pady=5)

        # OUTPUT BOX
        self.output = ctk.CTkTextbox(self, width=650, height=250)
        self.output.pack(pady=10)


    def add_student(self):
        student_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()

        if not validate_student_id(student_id):
            self.show("Invalid ID!")
            return

        if not validate_name(name):
            self.show("Invalid name!")
            return

        if not validate_age(age):
            self.show("Invalid age!")
            return

        student = Student(student_id, name, int(age), email="")
        success = self.manager.add_student(student)

        if success:
            self.show("Student added successfully!")
        else:
            self.show("Duplicate ID not allowed!")

    def view_students(self):
        students = self.manager.get_all()
        self.output.delete("1.0", "end")

        for s in students:
            self.output.insert("end", f"{s.id} | {s.name} | {s.age}\n")

    def search_student(self):
        student = self.manager.find_by_id(self.id_entry.get().strip())

        if student:
            self.show(f"{student.id} | {student.name} | {student.age}")
        else:
            self.show("Not found")

    def delete_student(self):
        success = self.manager.delete_student(self.id_entry.get().strip())

        if success:
            self.show("Deleted successfully")
        else:
            self.show("Not found")

    def show(self, message):
        self.output.delete("1.0", "end")
        self.output.insert("end", message)