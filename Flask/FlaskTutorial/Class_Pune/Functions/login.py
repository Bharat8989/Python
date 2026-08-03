from flask import Flask, request, jsonify
import xmltodict  # Essential for processing XML into a dictionary

app = Flask(__name__)

# --- ROUTE 1: For Handling JSON Data ---
@app.route('/user', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json() or {}
        
        name = str(data.get('name'))
        email = str(data.get('email'))
        age = int(data.get('age', 0)) # Added 0 fallback to prevent conversion crashes
        
        response_data = {
            "user": {
                "name": name,
                "email": email,
                "age": age
            }
        }
    return jsonify(response_data)


# --- ROUTE 2: For Handling XML Data ---
@app.route('/user/xml', methods=['POST'])  # Explicitly allow POST methods
def login_xml():
    # 1. Capture the raw text body from the incoming request
    raw_data = request.data
    
    if not raw_data:
        return jsonify({"error": "Empty body received"}), 400
        
    try:
        # 2. Parse the raw string into a readable Python dictionary
        parsed_xml = xmltodict.parse(raw_data)
        
        # 3. Look inside your root tag wrapper (e.g., <request>)
        data = parsed_xml.get('request', {})
        
        # 4. Read the variables using standard dict retrieval keys
        name = str(data.get('name'))
        email = str(data.get('email'))
        age = int(data.get('age', 0))
        
        # 5. Pack the parsed data into your target layout schema
        response_data = {
            "user": {
                "name": name,
                "email": email,
                "age": age
            }
        }
        return jsonify(response_data), 200
        
    except Exception as e:
        return jsonify({"error": "Invalid XML configuration", "details": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
