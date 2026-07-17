import mysql.connector
db =mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bharat@1297",
    database="flaskdb"
)
cursor = db.cursor()