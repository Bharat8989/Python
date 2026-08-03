import os
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Configure the directory where uploaded files will be stored
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory actually exists on your server
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload_id', methods=['POST', 'GET'])
def upload_id():
    # --- 1. HANDLING THE GET METHOD (SHOW FILE) ---
    if request.method == 'GET':
        user_id = request.args.get('id')
        
        if not user_id:
            return jsonify({'error': 'Missing ID parameter in URL query string'}), 400
            
        # Example: Assume file names map to the ID (e.g., "123.jpg", "123.png")
        # In a real app, you would query a database to find the exact filename for this ID
        filename = f"{user_id}.jpg" 
        
        # Check if the requested file actually exists on disk
        if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
            return jsonify({'error': f'File {filename} not found for ID {user_id}'}), 404
            
        # Safely streams the file directly to the client browser
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    # --- 2. HANDLING THE POST METHOD (SAVE FILE) ---
    if request.method == 'POST':
        if 'file' not in request.files or 'id' not in request.form:
            return jsonify({'error': 'Missing file or ID in form-data'}), 400

        file = request.files['file']
        id_from_form = request.form['id']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400


        file_extension = os.path.splitext(file.filename)[1]
        secure_filename = f"{id_from_form}{file_extension}"
        
        # Save to your configured uploads folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename)
        file.save(file_path)

        return jsonify({
            'message': 'File uploaded and saved successfully',
            'saved_as': secure_filename,
            'received_id': id_from_form
        }), 200

if __name__ == '__main__':
    app.run(debug=True)


