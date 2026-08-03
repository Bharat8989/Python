import os
from flask import Flask, request, jsonify

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload-video', methods=['POST'])
def upload_video():
    # 1. Grab text data if sent
    video_title = request.form.get('title', 'Untitled')
    
    # 2. Grab the video file using the Key name from Postman
    video = request.files.get('video')
    
    if not video:
        return jsonify({"error": "No video file provided"}), 400
        
    # 3. Save the file locally
    file_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(file_path)
    
    return jsonify({
        "message": "Video uploaded successfully",
        "title": video_title,
        "saved_to": file_path
    }), 200


if __name__=="__main__":
    app.run(debug=True)