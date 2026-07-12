from flask import Blueprint, jsonify,request
from validations.AuthValidation import register_user_schema 
from marshmallow import ValidationError


auth_route=Blueprint("AuthRoute",__name__)

@auth_route.route('/register',methods=['POST'])
def register():
   try:
       data=register_user_schema.load(request.json)  
       return {"message": "User registered successfully", "data": data}, 201
    
   except ValidationError as e:
       return {'message': 'Validation failed', 'errors': e.messages}, 400
        
   except Exception as e:
        return {"message": "An internal error occurred", "details": str(e)}, 500
    

