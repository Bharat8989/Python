from flask import Blueprint
from model.user_model import user_model 
# obj =user_model()
user_bp = Blueprint("user", __name__ ,url_prefix='/user')

@user_bp.route("/getall")
def user_getall_controller():
    obj=user_model()
    return obj.user_getall_model()