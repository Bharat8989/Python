import re
from repository.student_repo import StudentRepository
from models.student import Student

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

class StudentService:
    @staticmethod
    def create_student(data):
        if not data or not isinstance(data, dict):
            raise ValueError("Request body must be a valid JSON object.")

        name = str(data.get('name', '')).strip()
        email = str(data.get('email', '')).strip()
        course = str(data.get('course', '')).strip()
        age_raw = data.get('age')

        if not name or not email or age_raw is None or age_raw == '' or not course:
            raise ValueError("All fields (name, email, age, course) are required.")

        try:
            age = int(age_raw)
        except (TypeError, ValueError):
            raise ValueError("Age must be a valid integer.")

        if age < 1 or age > 120:
            raise ValueError("Age must be between 1 and 120.")

        if not EMAIL_REGEX.match(email):
            raise ValueError("Please provide a valid email address.")

        new_student = Student(
            name=name,
            email=email,
            age=age,
            course=course
        )
        student_id = StudentRepository.save(new_student)
        return {"message": "Student registered successfully", "id": student_id}

    @staticmethod
    def fetch_all_students():
        students = StudentRepository.get_all()
        return [student.to_dict() for student in students]

