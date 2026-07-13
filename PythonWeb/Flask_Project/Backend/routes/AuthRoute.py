from flask import Blueprint, request
from validations.AuthValidation import register_user_schema
from config.mongodb import mongo

from marshmallow import ValidationError
import bcrypt
import jwt

auth_route = Blueprint("AuthRoute", __name__)

@auth_route.route("/register", methods=["POST"])
def register():

    try:

        data = register_user_schema.load(request.json)

        hashed_password = bcrypt.hashpw(
            data["password"].encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        data["password"] = hashed_password

        result = mongo.db.users.insert_one(data)

        token = jwt.encode(
            {"user_id": str(result.inserted_id)},
            "secret",
            algorithm="HS256"
        )

        return {
            "message": "User Registered",
            "token": token
        }, 201

    except ValidationError as e:
        return {"errors": e.messages}, 400

    except Exception as e:
        return {"error": str(e)}, 500