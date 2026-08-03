import os
from flask import Flask, request, jsonify, send_from_directory
from flask import url_for


app = Flask(__name__)

# Define the folder name where uploaded files will be saved
UPLOAD_FOLDER = 'uploaded_pdf'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the folder automatically if it does not exist on your computer
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Set of allowed extensions for PDF files
ALLOWED_EXTENSIONS = {'pdf'}


# Function to check if the uploaded file has a valid PDF extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    # Check if the 'pdf' key is present in the request form-data
    if 'pdf' not in request.files:
        return jsonify({"error": "No PDF part in the form-data"}), 400
    
    # Retrieve the file object using the 'pdf' key
    file = request.files.get('pdf')

    # Check if the user submitted an empty field without selecting a file
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400
    
    # Check if the file format is allowed (pdf in this case)
    if not allowed_file(file.filename):
        return jsonify({'error': 'add the pdf only that formate (.pdf)'}), 400
    
    # Construct the full storage path to save the file inside the folder
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    # Save the file to the target location on the server
    file.save(save_path)
    
    # Return a success response along with file details
    return jsonify({
        "message": "File uploaded successfully!",
        "file_name": file.filename,
        "saved_at": save_path
    }), 201


# FIX 1 & 2: Differentiated unique endpoints and explicit mimetype definition
@app.route('/show-pdf/file/<filename>', methods=['GET'])
def show_pdf(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, mimetype='application/pdf')


@app.route('/show-pdf/latest', methods=['GET'])
def show_latest_pdf():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    
    if not files:
        return jsonify({"error": "No PDFs uploaded yet"}), 404
        
    full_paths = [os.path.join(app.config['UPLOAD_FOLDER'], f) for f in files]
    latest_file = max(full_paths, key=os.path.getmtime)
    filename = os.path.basename(latest_file)
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, mimetype='application/pdf')


@app.route('/show-pdf', methods=['GET'])
def show_pdf_json():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    
    if not files:
        return jsonify({"error": "No PDFs uploaded yet"}), 404
    
    # Create a list of dictionaries containing file names and their URLs
    full_paths = [os.path.join(app.config['UPLOAD_FOLDER'], f) for f in files]
    latest_file = max(full_paths, key=os.path.getmtime)
    filename = os.path.basename(latest_file)
    
    file_size = os.path.getsize(latest_file) 
    
    view_url = f"http://127.0.0.1:5000/show-pdf/file/{filename}"
    
    return jsonify({
        "status": "success",
        "message": "Latest PDF found",
        "pdf_details": {
            "file_name": filename,
            "file_size_bytes": file_size,
            "view_url": view_url
        }
    }), 200


if __name__ == '__main__':
    # Start the Flask development server in debug mode
    app.run(debug=True)
