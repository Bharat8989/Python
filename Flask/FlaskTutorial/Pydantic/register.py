# from flask import Flask, request, jsonify
# from pydantic import BaseModel, EmailStr, Field, ValidationError

# app = Flask(__name__)

# # 1. Define the validation blueprint
# class UserTestSchema(BaseModel):
#     username: str = Field(min_length=3, max_length=100)
#     email: EmailStr
#     mobile_number: str = Field(min_length=10, max_length=15)
#     password: str = Field(min_length=8)

# # 2. Create the testing route
# @app.route("/test-validation", methods=['POST'])
# def test_validation():
#     try:
#         # Get data from Postman
#         json_data = request.get_json(force=True)
        
#         # Validate data using Pydantic
#         validated_data = UserTestSchema(**json_data)
        
#         # If valid, return the clean data back to Postman
#         return jsonify({
#             "status": "Success",
#             "message": "Data is clean and valid!",
#             "data": validated_data.model_dump() # Converts Pydantic object back to dict
#         }), 200

#     except ValidationError as e:
#         # If invalid, return the errors back to Postman
#         return jsonify({
#             "status": "Validation Failed",
#             "errors": e.errors()
#         }), 400

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
from pydantic import BaseModel, EmailStr, Field, ValidationError

app = Flask(__name__)

# 1. RAM Data Store (In-Memory Database)
# This lives completely inside your RAM while the application runs.
RAM_DATA_STORE = []

# 2. Define the Pydantic Schema
class UserTestSchema(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    email: EmailStr
    mobile_number: str = Field(min_length=10, max_length=15)
    password: str = Field(min_length=8)

# 3. Route to Validate and Store Data
@app.route("/test-validation", methods=['POST'])
def test_validation():
    try:
        # Fetch raw data from Postman
        json_data = request.get_json(force=True)
        
        # DESERIALIZATION & VALIDATION
        # Pydantic v2 recommended method to parse dictionary
        validated_user = UserTestSchema.model_validate(json_data)
        
        # validated_user = UserTestSchema(**json_data)
        
        # SERIALIZATION
        # Convert Pydantic object into a standard python dictionary to save
        clean_user_dict = validated_user.model_dump()
        
        # STORE IN RAM: Appending the dict into our RAM array list
        RAM_DATA_STORE.append(clean_user_dict)
        
        # Return success with the entire RAM storage to inspect it
        return jsonify({
            "status": "Success",
            "message": "Data validated and stored in RAM successfully!",
            "current_users_in_ram": RAM_DATA_STORE,
            "total_users_count": len(RAM_DATA_STORE)
        }), 200

    except ValidationError as e:
        return jsonify({
            "status": "Validation Failed",
            "errors": e.errors()
        }), 400

# 4. Route to view current RAM status anytime
@app.route("/view-ram", methods=['GET'])
def view_ram():
    return jsonify({
        "info": "All active users stored inside system RAM",
        "data": RAM_DATA_STORE,
        "count": len(RAM_DATA_STORE)
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
