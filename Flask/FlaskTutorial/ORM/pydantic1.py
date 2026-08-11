from flask import Flask, jsonify, request  
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel, EmailStr, Field
from flask_pydantic import validate

app = Flask(__name__)
 
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:Bharat%401297@localhost/college"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
 
db = SQLAlchemy(app)
 
 
class Student(db.Model):
    __tablename__ = "student"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    marks = db.Column(db.Integer)
 
 
class StudentCreateSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr  
    marks: int = Field(..., ge=0, le=100) 


class StudentUpdateSchema(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    email: EmailStr | None = None
    marks: int | None = Field(None, ge=0, le=100)


@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    return jsonify([
        {
            "id": s.id,
            "name": s.name,
            "email": s.email,
            "marks": s.marks
        }
        for s in students
    ])
 
 
@app.route("/student", methods=["POST"])
@validate(body=StudentCreateSchema) 
def save_student(body: StudentCreateSchema): 
    
    student = Student(**body.model_dump())
 
    db.session.add(student)
    db.session.commit()
 
    return {
        "message": "Student saved successfully",
        "id": student.id
    }
   

@app.route("/student/<int:id>", methods=["PUT"])
@validate(body=StudentUpdateSchema) 
def update_student(id, body: StudentUpdateSchema):
 
    student = db.session.get(Student, id)
 
    if student is None:
        return jsonify({"message": "Student not found"}), 404
 
    student.name = body.name if body.name is not None else student.name
    student.email = body.email if body.email is not None else student.email
    student.marks = body.marks if body.marks is not None else student.marks
 
    db.session.commit()
 
    return jsonify({
        "message": "Student updated successfully",
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "marks": student.marks
    })
 
 
@app.route("/student/<int:id>", methods=["DELETE"])
def delete_student(id):
 
    student = db.session.get(Student, id)
 
    if student is None:
        return jsonify({"message": "Student not found"}), 404
 
    db.session.delete(student)
    db.session.commit()
 
    return jsonify({
        "message": "Student deleted successfully",
        "id": id
    })
 
 
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
 
    print("\n========== REGISTERED ENDPOINTS ==========")
    for rule in app.url_map.iter_rules():
        methods = ", ".join(sorted(rule.methods - {"HEAD", "OPTIONS"}))
        print(f"{methods:10} {rule}")
    print("==========================================\n")
 
    app.run(debug=True)
