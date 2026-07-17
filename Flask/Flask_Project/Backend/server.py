from app import create_app
from flask_cors import CORS

app = create_app()

CORS(app)

@app.route("/")
def home():
    return {"message": "Welcome"}

if __name__ == "__main__":
    app.run(debug=True, port=8000)