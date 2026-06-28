import mysql.connector
import json
class user_model():
    def __init__(self):
        # connections code 
        try:
            self.con=mysql.connector.connect(host='localhost',user='root',password='Bharat@1297',database='flaskdb')
            self.cur=self.con.cursor(dictionary=True)

            print("connection establish")
        except:
            print("some error")
   

    def user_getall_model(self):
        #query executions code 
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)


        else:
            return "no data found"
