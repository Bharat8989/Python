from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from config.db import db
from controllers.student_controller import student_blueprint
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path='')
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL', 'mysql+pymysql://root:Bharat%401297@localhost/js')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Warning: Database initialization error: {e}")

app.register_blueprint(student_blueprint, url_prefix='/api')

@app.route('/')
def index():
    if os.path.exists(os.path.join(FRONTEND_DIR, 'index.html')):
        return send_from_directory(FRONTEND_DIR, 'index.html')
    return jsonify({
        "status": "online",
        "message": "Student Registration API is active",
        "endpoints": ["/api/students"]
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

