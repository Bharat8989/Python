from flask import Flask

app = Flask(__name__)

from controller.user_controller import user_bp
# from controller import *
# from controller.product_controller import product_bp

app.register_blueprint(user_bp)
# app.register_blueprint(product_bp)

# routing is the process of mapping a url to a python functions 
@app.route("/")

def home():
    return "this is home page "

if __name__ == "__main__":
    app.run(debug=True)