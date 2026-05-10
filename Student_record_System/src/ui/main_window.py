import customtkinter as ctk
from src.data.student_manager import StudentManager
from src.models.student import Student
from src.utils.validators import validate_student_id, validate_name, validate_age


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.title("Student Record System")
        self.geometry("700x500")

        self.manager = StudentManager()
        self.header = ctk.CTkLabel(
            self,
            text="Welcome to Student Record System",
            font=("Times New Roman", 28),
            text_color="white"
        )
        #Header and types
        self.header.grid(
            row=0,
            column=0,
            columnspan=3,
            pady=20
        )

        
        student_id = ctk.CTkLabel(
            self,
            text="Student ID"
        )
        student_id.grid(
            row=1,
            column=0,
            padx=5,
            pady=(10, 0)
        )

        name = ctk.CTkLabel(
            self,
            text="Name"
        )
        name.grid(
            row=1,
            column=1,
            padx=5,
            pady=(10, 0)
        )

        age = ctk.CTkLabel(
            self,
            text="Age"
        )
        age.grid(
            row=1,
            column=2,
            padx=5,
            pady=(10, 0)
        )

        #  ENTRIES 
        self.id_entry = ctk.CTkEntry(
            self,
            width=180,
            placeholder_text="Enter ID"
        )

        self.id_entry.grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

        self.name_entry = ctk.CTkEntry(
            self,
            width=180,
            placeholder_text="Enter Name"
        )

        self.name_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        self.age_entry = ctk.CTkEntry(
            self,
            width=180,
            placeholder_text="Enter Age"
        )

        self.age_entry.grid(
            row=2,
            column=2,
            padx=5,
            pady=5
        )

        #Buttons
        add = ctk.CTkButton(
            self,
            text="Add Student",
            command=self.add_student,
            width=150
        )
        add.grid(
            row=3,
            column=0,
            padx=5,
            pady=15
        )

        view = ctk.CTkButton(
            self,
            text="View Students",
            command=self.view_students,
            width=150
        )
        view.grid(
            row=3,
            column=1,
            padx=5,
            pady=15
        )

        Search_students = ctk.CTkButton(
            self,
            text="Search Student",
            command=self.search_student,
            width=150
        )
        Search_students.grid(
            row=3,
            column=2,
            padx=5,
            pady=15
        )
        delete = ctk.CTkButton(
            self,
            text="delete a student",
            command=self.delete_student,
            width=150
        )
        delete.grid(
            row=4,
            column=1,
            padx=5,
            pady=15
        )
        #Textbox
        self.output = ctk.CTkTextbox(
            self,
            width=650,
            height=200,
            state = "disabled"
        )

        self.output.grid(
            row=5,
            column=0,
            columnspan=3,
            padx=10,
            pady=10
        )
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
        self.output.configure(state="normal")
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
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("end", message)
        self.output.configure(state="disabled")