from flask import Blueprint, request, jsonify
from flask_mysqldb import MySQLdb

# 1. Create a Blueprint for user-related routes
user_blueprint = Blueprint('user_blueprint', __name__)


# ---- 1. AUTOMATICALLY CREATE THE TABLE ----
@user_blueprint.route('/create-table', methods=['GET'])
def create_alluser_table():
    # Local import inside the function breaks the circular loop completely
    from flask_mysql import mysql  
    
    cur = mysql.connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS alluser (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        mobile_number VARCHAR(15) NOT NULL
    )
    """
    cur.execute(create_table_query)
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Table 'alluser' created successfully with UNIQUE constraints!"}), 200


# ---- 2. GET ALL USERS (GET METHOD) ----
@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    from flask_mysql import mysql  # Local import
    
    cur = mysql.connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM alluser")
    data = cur.fetchall()
    cur.close()
    return jsonify(data), 200


# ---- 3. CREATE A NEW USER (POST METHOD) ----
@user_blueprint.route('/users', methods=['POST'])
def add_new_user():
    from flask_mysql import mysql  # Local import
    
    data = request.get_json()
    username = data['username']
    email = data['email']
    mobile = data['mobile_number']

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO alluser (username, email, mobile_number) VALUES (%s, %s, %s)",
        (username, email, mobile)
    )
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User added successfully!"}), 201


# ---- 4. UPDATE USER DETAILS (PUT METHOD) ----
@user_blueprint.route('/users/<int:id>', methods=['PUT'])
def update_user_info(id):
    from flask_mysql import mysql  # Local import
    
    data = request.get_json()
    username = data['username']
    email = data['email']
    mobile = data['mobile_number']

    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE alluser SET username = %s, email = %s, mobile_number = %s WHERE id = %s",
        (username, email, mobile, id)
    )
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": f"User with ID {id} updated successfully!"}), 200


# ---- 5. DELETE A USER (DELETE METHOD) ----
@user_blueprint.route('/users/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    from flask_mysql import mysql  # Local import
    
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM alluser WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": f"User with ID {id} deleted successfully!"}), 200
