"""
Docstring for Student_record_System.src.models.student
"""

class Student:
    def __init__(self, student_id: str, name: str, age: int, email: str, grades=None):
        self.id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.grades = grades if grades is not None else []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "grades": self.grades,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data.get("id"),
            name=data.get("name"),
            age=data.get("age"),
            email=data.get("email"),
            grades=data.get("grades", [])
        )
        
    