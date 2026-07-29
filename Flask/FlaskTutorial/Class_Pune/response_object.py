from flask import Flask, jsonify, make_response

app = Flask(__name__)

# 1. Simple Return and Success Response (200 OK)
@app.route('/text-response/')
def text_response():
    # Returning plain text string with default 200 OK status code
    return "This is a simple plain text success response!"


# 2. Jsonify Response (Standard for modern APIs)
@app.route('/json-response/')
def json_response():
    user_info = {
        "status": "success",
        "user_id": 101,
        "role": "admin"
    }
    # jsonify() converts dict to JSON and sets content-type header automatically
    return jsonify(user_info), 200


# 3. Custom Response with make_response() and Custom Headers
@app.route('/custom-response/')
def custom_response():
    # Creating a custom response object
    response_data = jsonify({"message": "Data generated successfully"})
    response = make_response(response_data, 201) # 201 status code means 'Created'
    
    # Setting custom Response Headers
    response.headers['X-Custom-Header'] = 'Flask-Response-Token-XYZ'
    response.headers['Access-Control-Allow-Origin'] = '*' # Allows cross-origin access
    
    return response


# 4. Error Responses (Client and Server Errors)
@app.route('/error-trigger/<int:code>/')
def trigger_error(code):
    # 400: Bad Request (Client sent invalid data)
    if code == 400:
        return jsonify({"error": "Bad Request", "details": "Missing required fields"}), 400
        
    # 404: Not Found (Resource does not exist)
    elif code == 404:
        return jsonify({"error": "Resource Not Found", "id_requested": code}), 404
        
    # 500: Internal Server Error (Something crashed on server side)
    elif code == 500:
        return jsonify({"error": "Internal Server Error", "msg": "Database connection failed"}), 500
        
    # Fallback default success response
    return jsonify({"message": "Valid code received"}), 200

if __name__ == '__main__':
    app.run(debug=True)
