import os

from flask import Flask
from dotenv import load_dotenv

from config.mongodb import mongo
from routes.AuthRoute import auth_route

load_dotenv()


def create_app():

    app = Flask(__name__)

    app.config["MONGO_URI"] = os.getenv("MONGO_URI")

    mongo.init_app(app)

    app.register_blueprint(auth_route, url_prefix="/api")

    return app

# import os
# from flask import Flask 
# from dotenv import load_dotenv
# import mysql.connector  # 1. Import the MySQL connector

# load_dotenv()

# def create_app():
#     app = Flask(__name__)
    
#     # 2. Establish connection using variables from .env
#     try:
#         db_connection = mysql.connector.connect(
#             host=os.getenv('MYSQL_HOST'),
#             user=os.getenv('MYSQL_USER'),
#             password=os.getenv('MYSQL_PASSWORD'),
#             database=os.getenv('MYSQL_DATABASE')
#         )
        
#         # 3. Attach the connection object to your app
#         app.db = db_connection
#         print("MySQL Database Connected Successfully!")
        
#     except mysql.connector.Error as e:
#         print("Failed to connect to MySQL:", e)
        
#     return app
