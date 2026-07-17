from flask import Blueprint, request
from model.user_model import user_model

user_bp = Blueprint("user", __name__, url_prefix="/user")


# GET ALL USERS
@user_bp.route("/getall", methods=["GET"])
def user_getall_controller():
    obj = user_model()
    return obj.user_getall_model()


# INSERT USER
@user_bp.route("/addone", methods=["POST"])
def user_addone_controller():
    obj = user_model()
    return obj.user_addone_model(request.form)

# Update user

@user_bp.route("/update", methods=["PUT"])
def user_update_controller():
    obj = user_model()
    return obj.user_update_model(request.form)