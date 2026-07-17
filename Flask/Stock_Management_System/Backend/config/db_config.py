# Backend/config/db_config.py
import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bharat@1297",
            database="stock"
        )
        return db
    except Error:
        return None

def init_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bharat@1297"
        )
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS stock")
        cursor.close()
        db.close()

        db = get_db_connection()
        if db:
            cursor = db.cursor()
            table_query = """
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                stock INT NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(table_query)
            db.commit()
            print("MySQL Database & Tables verified/created successfully!")
            cursor.close()
            db.close()
    except Error as e:
        print(f"Error during automatic database initialization: {e}")
           
           