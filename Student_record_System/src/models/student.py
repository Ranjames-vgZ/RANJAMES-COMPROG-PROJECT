class Student:

    def __init__(self, student_id: str, name: str, age: str, email: str, grade=None):
        self.id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.grade = grade if grade is not None else []

    def to_dict(self):

        return{
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "grade": self.grade,
        }
    @classmethod
    def from_dict(clss, data):
        return clss(
            Student_id=data.get("id"),
            name=data.get("name"),
            age=data.get("age"),
            email=data.get("email"),
            grade=data.get("grades", [])
        )
        
    