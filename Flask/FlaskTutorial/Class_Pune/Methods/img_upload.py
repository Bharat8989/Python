import os
from flask import Flask, request, jsonify,send_from_directory

app = Flask(__name__)

# Define the folder name where uploaded files will be saved
UPLOAD_FOLDER = 'uploaded_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the folder automatically if it does not exist on your computer
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Set of allowed extensions for image files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','pdf'}


# Function to check if the uploaded file has a valid image extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload-image', methods=['POST'])
def upload_image():
    # Check if the 'image' key is present in the request form-data
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the form-data"}), 400
    
    # Retrieve the file object using the 'image' key
    file = request.files.get('image')

    # Check if the user submitted an empty field without selecting a file
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400
    
    # Check if the file format is allowed (png, jpg, jpeg, gif)
    if not allowed_file(file.filename):
        return jsonify({'error': 'add the img only that formate (.png ,.jpg, .jpeg,.gif,.pdf)'}), 400
    
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
    
    
@app.route('/show-img/<filename>', methods=['GET'])
def show_image(filename):
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/show-img', methods=['GET'])
def show_latest_image():
    
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    
    
    if not files:
        return jsonify({"error": "No images uploaded yet"}), 404
        
   
    full_paths = [os.path.join(app.config['UPLOAD_FOLDER'], f) for f in files]
    latest_file = max(full_paths, key=os.path.getmtime)
    filename = os.path.basename(latest_file)
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    # Start the Flask development server in debug mode
    app.run(debug=True)
