# # from flask import Flask, request 
# # from flask import render_template,jsonify

# # app = Flask(__name__)


# # @app.route('/')
# # def home():
# #     return render_template('index.html')
    
# # @app.route("/login", methods=["POST"])
# # def login():
# #     data=request.json

# #     username = data.get("username")
# #     password = data.get("password")
# #     print(f"Username: {username}  Password: {password}")
# #     return jsonify(data)

# # @app.route("/upload", methods=["POST"])
# # def upload():

# #     file = request.files["photo"]

# #     file.save(file.filename)

# #     return "Uploaded Successfully"

# # @app.route("/student/<int:id>")
# # def student(id):

# #     student = {
# #         "id":id,
# #         "name":"Bharat",
# #         "course":"Python"
# #     }

# #     return jsonify({
# #         "status":1,
# #         "message":"Student Found",
# #         "data":student
# #     }), 200

# # if __name__ == "__main__":
# #     app.run(debug=True)

# # from flask import Flask,session

# # from controller.user_controller import user_bp

# # app=Flask(__name__)

# # app.register_blueprint(user_bp)

# # @app.route('/')
# # def home():
# #     return "this is home page "

# # app.secret_key = "secret"

# # @app.route("/login")
# # def login():

# #     session["user"] = "Bharat"

# #     return "Login Success"


# # @app.route("/dashboard")
# # def dashboard():

# #     if "user" in session:

# #         return f"Welcome {session['user']}"

# #     return "Login First"


# # @app.route("/logout")
# # def logout():

# #     session.pop("user", None)

# #     return "Logout Success"

# # if __name__=="__main__":
# #     app.run(debug=True)

# # from flask import Flask, make_response,request

# # app = Flask(__name__)

# # @app.route("/")
# # def home():

# #     response = make_response("Cookie Created")

# #     response.set_cookie("username", "Bharat")
# #     # print(result)
# #     # username=request.cookies.get('username')
# #     # print('username1')

# #     return response

# # if __name__ == "__main__":
# #     app.run(debug=True)

# from flask import Flask, request,make_response

# app = Flask(__name__)

# # @app.route("/")
# # def home():

# #     response = make_response("Cookie Created")

# #     response.set_cookie("username", "Bharat")
# #     # print(result)
# #     # username=request.cookies.get('username')
# #     # print('username1')

# #     return response

# # @app.route("/profile")
# # def profile():

# #     username = request.cookies.get("username")

# #     return f"Welcome {username}"

# # @app.route("/login", methods=["POST"])
# # def login():

# #     response = make_response("Login Success")

# #     if request.form.get("remember"):

# #         response.set_cookie(
# #             "user",
# #             "Bharat",
# #             max_age=60*60*24*30
# #         )

# #     return response

# from werkzeug.security import generate_password_hash,check_password_hash
# @app.route('/')
# def home():
#     password='1343333'
#     hashed_password=generate_password_hash(password)
#     print(hashed_password)
#     return "this is hash code "
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# --- SMTP 
app.config['MAIL_SERVER'] = 'smtp.gmail.com'         
app.config['MAIL_PORT'] = 587                         
app.config['MAIL_USE_TLS'] = True                    
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'bk2905190@gmail.com'
app.config['MAIL_PASSWORD'] = 'xwdm bsbu muob gydh'  
app.config['MAIL_DEFAULT_SENDER'] = 'kadamb208@gmail.com'


mail = Mail(app)

@app.route('/send-email')
def send_email():
    try:
        msg = Message(
            "Welcome",
            recipients=["kadamb208@gmail.com"] 
        )
        msg.body = "Registration Successful"
        
        
        mail.send(msg)
        return "Mail Sent Successfully! 👍"
        
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
