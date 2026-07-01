# from flask import Flask
# from controller.auth_controller import auth_bp
# # from controller.student_controller import student_bp

# def create_app():

#     app = Flask(__name__)

#     app.secret_key = "student_management_secret_key"

#     app.register_blueprint(auth_bp)
#     # app.register_blueprint(student_bp)

#     return app

# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=True)

# python quick revision 

from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    name ='bharat'
    age=21
    percentage=56.3
    is_student=True
    str="this"
    print(type(str))
    print(type(name))
    print(type(age))
    print(type(is_student))
    print(type(percentage))
    return render_template('index.html',name=name,age=age,percentage=percentage,is_student=is_student)

if __name__ == '__main__':
    app.run(debug=True)