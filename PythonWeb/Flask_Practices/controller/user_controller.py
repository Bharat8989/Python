from flask import Blueprint, request, jsonify
from models.user_model import UserModel
from flask import session

user_bp = Blueprint("user", __name__)
obj = UserModel()

# Changed to POST because you are adding/inserting a user
@user_bp.route("/users", methods=["POST"])
def add_user():
    # 1. Safely extract JSON data
    data = request.get_json(silent=True)
    
    if not data:
        return jsonify({"status": 0, "message": "Invalid JSON body"}), 400

    # 2. Run validations BEFORE inserting into the database
    if not data.get("name"):
        return jsonify({"status": 0, "message": "Name Required"}), 400
    email =data.get("email")
    if not email:
        return jsonify({"status": 0,"message":"email required"}),400
    if "@" not in email:
        return jsonify({"status": 0, "message": "Invalid Email Format"}), 400

    phone = data.get("phone")
    if not phone:
        return jsonify({"status": 0, "message": "Phone Required"}), 400
    
    phone = str(phone).strip()
    
    if not phone.isdigit() or len(phone) != 10:
        return jsonify({
            "status": 0, 
            "message": "Invalid Phone Number. Must be exactly 10 digits."
        }), 400
    # 3. Database operation after validation passes
    result = obj.insert_user(data)

    return jsonify({
        "status": 1,
        "message": "User added successfully",
        "result": result
    }), 201


@user_bp.route('/users/read', methods=['GET'])
def read_user():
    data = obj.get_users()
    return jsonify(data), 200

@user_bp.route("/dashboard")
def dashboard():

    user = session.get("user")

    return f"Welcome {user}"