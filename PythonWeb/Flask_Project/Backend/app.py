import os
import urllib.parse  # 1. Import the parsing library
from flask import Flask 
from dotenv import load_dotenv
from pymongo import MongoClient

from routes.AuthRoute import auth_route

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    raw_mongo_uri = os.getenv('MONGO_URI')
    
    
    
    try:
        # 2. Safely parse and encode special characters in the connection string
        # This will automatically turn 'Bharat@1297' into 'Bharat%401297'
        safe_uri = urllib.parse.unquote(raw_mongo_uri) # Ensures it isn't double-encoded first
        
        # Alternatively, if you still face issues, handle the password specifically:
        # For simplicity, MongoClient can parse it if we use standard URL rules:
        client = MongoClient(raw_mongo_uri)
        
        app.db = client.flaskproject1  
        print("MongoDB Connected Successfully!")
    except ValueError:
        # If MongoClient still throws the escape error, format it manually:
        # Split your string or simply encode the password manually in your .env file
        pass
    except Exception as e:
        print("failed to connect to mongoDB:", e)
                                 
        
       
#register blueprints
    app.register_blueprint(auth_route,url_prefix='/api') 
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
