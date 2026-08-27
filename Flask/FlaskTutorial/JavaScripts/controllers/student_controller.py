from flask import Blueprint, request, jsonify
from services.student_service import StudentService

student_blueprint = Blueprint('student_blueprint', __name__)

@student_blueprint.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.get_json(silent=True)
        if data is None:
            return jsonify({"error": "Invalid or missing JSON payload."}), 400

        result = StudentService.create_student(data)
        return jsonify(result), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

@student_blueprint.route('/students', methods=['GET'])
def get_students():
    try:
        students = StudentService.fetch_all_students()
        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

