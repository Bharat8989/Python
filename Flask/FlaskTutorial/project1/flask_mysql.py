from flask import Flask
from config.config import Config
from flask_mysqldb import MySQL


app = Flask(__name__)

# Database Configuration
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Bharat'
# app.config['MYSQL_DB'] = 'tutorial'

# load the file for the 
app.config.from_object(Config)

# mysql = MySQL(app)

mysql=MySQL(app) 
from routes.user_routes import user_blueprint


app.register_blueprint(user_blueprint)


@app.route('/')
def home():
    return "this is home page "




if __name__ == '__main__':
    app.run(debug=True)