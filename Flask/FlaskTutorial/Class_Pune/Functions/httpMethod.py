from flask import Flask, request, jsonify

app = Flask(__name__)

# Single route handling four different HTTP methods
@app.route('/api/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_user():
    
    # 1. GET Method: Read ID from the URL query parameters (e.g., /api/user?id=101)
    if request.method == 'GET':
        user_id = request.args.get('id')
        return f"Displaying information for User ID: {user_id}"

    # 2. POST Method: Read incoming JSON data from the request body
    elif request.method == 'POST':
        user_data = request.json
        return jsonify({"status": "Data saved successfully", "user": user_data}), 201

    # 3. PUT Method: Read form data submitted to update an existing record
    elif request.method == 'PUT':
        updated_name = request.form.get('name')
        return f"User name has been updated to: {updated_name}"

    # 4. DELETE Method: Handle the request to delete a record
    elif request.method == 'DELETE':
        return "User data has been deleted successfully."

if __name__ == '__main__':
    # Run the server in development mode with auto-reload enabled
    app.run(debug=True)
