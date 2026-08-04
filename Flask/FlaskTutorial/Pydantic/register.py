from flask import Flask, request, jsonify
from pydantic import BaseModel, EmailStr, Field, ValidationError

app = Flask(__name__)

# 1. Define the validation blueprint
class UserTestSchema(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    email: EmailStr
    mobile_number: str = Field(min_length=10, max_length=15)
    password: str = Field(min_length=8)

# 2. Create the testing route
@app.route("/test-validation", methods=['POST'])
def test_validation():
    try:
        # Get data from Postman
        json_data = request.get_json(force=True)
        
        # Validate data using Pydantic
        validated_data = UserTestSchema(**json_data)
        
        # If valid, return the clean data back to Postman
        return jsonify({
            "status": "Success",
            "message": "Data is clean and valid!",
            "data": validated_data.model_dump() # Converts Pydantic object back to dict
        }), 200

    except ValidationError as e:
        # If invalid, return the errors back to Postman
        return jsonify({
            "status": "Validation Failed",
            "errors": e.errors()
        }), 400

if __name__ == "__main__":
    app.run(debug=True)
