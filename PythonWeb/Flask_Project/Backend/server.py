from app import create_app
from flask_cors import CORS

app = create_app()

@app.route('/')
def index():
    return {'message': 'Welcome to the Flask API'}

CORS(app)  # Enables CORS for your entire app

if __name__ == "__main__":
    app.run(debug=True, port=8000)
