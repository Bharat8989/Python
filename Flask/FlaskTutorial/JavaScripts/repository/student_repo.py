from config.db import db
from models.student import Student

class StudentRepository:
    @staticmethod
    def save(student_data):
        try:
            db.session.add(student_data)
            db.session.commit()
            return student_data.id
        except Exception:
            db.session.rollback()
            raise

    @staticmethod
    def get_all():
        return Student.query.all()

    @staticmethod
    def get_by_id(student_id):
        return Student.query.get(student_id)

