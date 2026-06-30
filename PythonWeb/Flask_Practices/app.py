from flask import Flask
# from flask import Blueprint
from controller.user_controller import user_bp
from controller.product_controller import product_bp


app= Flask(__name__)




app.register_blueprint(user_bp)
app.register_blueprint(product_bp)

@app.route('/')
def home():
    return "this is home page "


# @app.route('/user/<name>')
# def user(name):
#     return f"he {name}"

if __name__ == '__main__':
    app.run(debug=True)