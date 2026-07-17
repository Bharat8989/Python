from flask import Flask

app = Flask(__name__)

from controller.user_controller import user_bp

app.register_blueprint(user_bp)

@app.route("/")
def home():
    return "This is Home Page"

if __name__ == "__main__":
    app.run(debug=True)