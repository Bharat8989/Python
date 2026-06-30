from config.db import db, cursor

class UserModel:

    # CREATE
    def insert_user(self, data):
        
        if not data:
            return {"status": 0, "message": "No data provided"}

        
        query = """
        INSERT INTO users (name, email, phone)
        VALUES (%(name)s, %(email)s, %(phone)s)
        """

       
        cursor.execute(query, data)

        
        db.commit()

        return {
            "status": 1,
            "message": "User Added Successfully"
        }
