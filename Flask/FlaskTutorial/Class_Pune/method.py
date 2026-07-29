from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory database
users_db = [
    {"id": 1, "username": "Rahul", "email": "rahul@email.com"},
    {"id": 2, "username": "Amit", "email": "amit@email.com"}
]

# 1. Route to view all users (GET) and add a new user (POST)
@app.route('/user/', methods=['GET', 'POST'])
def handle_user():
    
    # --- GET: Fetch all data or filter by name ---
    if request.method == 'GET':
        name = request.args.get('name')
        if name:
            # Filter users by name if provided in URL (e.g., /user?name=Rahul)
            filtered_users = [u for u in users_db if u['username'].lower() == name.lower()]
            return jsonify({"found_users": filtered_users})
        
        # If no query parameter, return the entire database
        return jsonify({"all_users": users_db})
        
    # --- POST: Create/Add a new user ---
    elif request.method == 'POST':
        # Read incoming JSON data from request body
        incoming_data = request.json
        
        # Validate that required fields are present
        if not incoming_data or 'username' not in incoming_data or 'email' not in incoming_data:
            return jsonify({"error": "Please provide username and email in JSON format"}), 400
            
        # Automatically generate a new incremental ID
        new_id = users_db[-1]['id'] + 1 if users_db else 1
        
        new_user = {
            "id": new_id,
            "username": incoming_data.get('username'),
            "email": incoming_data.get('email')
        }
        
        # Append the new user to our in-memory list
        users_db.append(new_user)
        
        return jsonify({
            "message": "User added successfully!",
            "added_user": new_user,
            "current_database": users_db
        }), 201


# 2. Route to update (PUT) and delete (DELETE) a specific user by ID
@app.route('/user/<int:user_id>', methods=['PUT', 'DELETE'])
def update_delete_user(user_id):
    
    # Search for the user with the matching ID
    user = next((u for u in users_db if u['id'] == user_id), None)
    
    # Return 404 error if user is not found
    if not user:
        return jsonify({"error": f"User with ID {user_id} not found!"}), 404

    # --- PUT: Update existing user data ---
    if request.method == 'PUT':
        incoming_data = request.json
        
        if incoming_data:
            # Update values only if they are passed in the JSON request
            user['username'] = incoming_data.get('username', user['username'])
            user['email'] = incoming_data.get('email', user['email'])
            
        return jsonify({
            "message": f"User {user_id} updated successfully!",
            "updated_user": user,
            "current_database": users_db
        })
        
    # --- DELETE: Remove the user from database ---
    elif request.method == 'DELETE':
        users_db.remove(user)
        return jsonify({
            "message": f"User {user_id} deleted successfully!",
            "current_database": users_db
        })

if __name__ == '__main__':
    app.run(debug=True)
