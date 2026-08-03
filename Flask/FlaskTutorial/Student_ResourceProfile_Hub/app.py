import os 
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Global list to store student data acting as a temporary database
students_db = []

@app.route('/', methods=['GET'])
def get_all_student():
    # Return all registered students from the list
    return jsonify({
        "message": "Welcome to Student Resource Profile Hub",
        "total_students": len(students_db),
        "students": students_db
    }), 200   


# 1. POST (form-data): To accept file + text data 
@app.route('/student/register', methods=['POST'])
def register_student():
    name = request.form.get('name')
    pdf_file = request.files.get('pdf_file')
    
    # Validation to prevent crash if data is missing
    if not name or not pdf_file:
        return jsonify({"error": "Missing name or pdf_file"}), 400
        
    # Append structured student data into global list
    student_data = {
        "name": name,
        "pdf_filename": pdf_file.filename,
        "marks": {},
        "email": None
    }
    students_db.append(student_data)
    return jsonify({"message": "Student registered successfully", "student": student_data}), 201  
  

# 2. POST (raw JSON): To add marks to a specific student
@app.route('/student/add-marks/<name>', methods=['POST'])
def add_marks(name):
    # force=True prevents 415 errors if content-type header is wrong
    data = request.get_json(force=True) 
    
    # Search for the student by name in the database list
    for student in students_db:
        if student['name'].lower() == name.lower():
            student['marks'] = data.get('marks', {})
            return jsonify({"message": "Marks added successfully", "student": student}), 201
            
    return jsonify({"error": "Student not found"}), 404


# 3. POST (x-www-form-urlencoded): To update credentials like email/login details
@app.route('/student/login', methods=['POST'])
def login_student():
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name') # match identity
    
    for student in students_db:
        if student['name'].lower() == name.lower():
            student['email'] = email
            return jsonify({"message": "Student logged in & profile synchronized", "student": student}), 200
            
    return jsonify({"message": "Authentication processed", "email": email}), 200


# 4. POST (binary): Upload raw stream directly as file
@app.route('/student/upload-raw-pdf', methods=['POST'])
def upload_binary():
    binary_data = request.data 
    # Save the incoming byte stream directly to a file
    with open('uploaded_file.pdf', 'wb') as f:
        f.write(binary_data)
        
    return jsonify({"message": "Binary data saved successfully as PDF"}), 200


# 5. PUT: Replaces the entire student object completely
@app.route('/student/update-all/<name>', methods=['PUT'])
def update_student_complete(name):
    data = request.get_json(force=True)
    
    for i, student in enumerate(students_db):
        if student['name'].lower() == name.lower():
            # Replace the entire dictionary content with incoming data
            students_db[i] = data
            return jsonify({"message": f"Student {name} completely overwritten", "updated_data": students_db[i]}), 200
            
    return jsonify({"error": "Student not found"}), 404


# 6. PATCH: Updates only specific keys without wiping other fields
@app.route('/student/update-partial/<name>', methods=['PATCH']) 
def update_student_partial(name):   
    data = request.get_json(force=True)
    
    for student in students_db:
        if student['name'].lower() == name.lower():
            # Dynamically update only the fields sent in the request
            student.update(data)
            return jsonify({"message": f"Student {name} partially updated", "student": student}), 200
            
    return jsonify({"error": "Student not found"}), 404
    

# 7. DELETE: Removes the student object from the list
@app.route('/student/delete/<name>', methods=['DELETE'])
def delete_student(name):
    for student in students_db:
        if student['name'].lower() == name.lower():
            # Remove record from database
            students_db.remove(student)
            return jsonify({"message": f"Student {name} deleted successfully."}), 200
            
    return jsonify({"error": "Student not found"}), 404


# 8. HEAD: Returns metadata headers only (No JSON content will appear in Postman Response Body)
@app.route('/student/head/<name>', methods=['HEAD'])
def get_student_head(name):
    # Construct empty context response to attach metadata headers
    response = jsonify({})
    response.headers['X-Student-Exists'] = 'True'
    response.headers['X-Database-Count'] = str(len(students_db))
    return response, 200
    

# 9. OPTIONS: Communicates allowed API communication properties
@app.route('/student/permissions', methods=['OPTIONS'])
def get_student_permissions():
    response = jsonify({"message": "Use headers to check allowed methods"})
    # Specify allowed actions for security/CORS pre-flight requests
    response.headers['Allow'] = 'GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS'
    return response, 200


if __name__ == '__main__':
    app.run(debug=True)
