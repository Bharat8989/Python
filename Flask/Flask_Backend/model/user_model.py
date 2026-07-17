import mysql.connector
from flask import jsonify


class user_model:

    def __init__(self):

        self.con = mysql.connector.connect(
            host="localhost", user="root", password="Bharat@1297", database="flaskdb"
        )

        self.con.autocommit = True
        self.cur = self.con.cursor(dictionary=True)

    # GET ALL USERS
    def user_getall_model(self):

        self.cur.execute("SELECT * FROM users")

        result = self.cur.fetchall()

        if len(result) > 0:
            return jsonify(result)

        return jsonify({"message": "No Data Found"}), 404

    # INSERT USER
    def user_addone_model(self, data):

        self.cur.execute(
            """
            INSERT INTO users(name,email,phone,role)
            VALUES(%s,%s,%s,%s)
            """,
            (data["name"], data["email"], data["phone"], data["role"]),
        )

        self.con.commit()

        return jsonify({"status": 1, "message": "User Added Successfully"})

   # Update User
    def user_update_model(self, data):

        self.cur.execute(
        """
        UPDATE users
        SET
            name=%s,
            email=%s,
            phone=%s,
            role=%s
        WHERE id=%s
        """,
        (
            data["name"],
            data["email"],
            data["phone"],
            data["role"],
            data["id"]
        )
    )

        self.con.commit()

        if self.cur.rowcount > 0:
            return "User Updated Successfully"
        else:
            return "Nothing to Update"
    