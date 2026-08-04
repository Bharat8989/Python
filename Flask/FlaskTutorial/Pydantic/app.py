from pydantic import BaseModel, EmailStr
import json

# 1. Define the Pydantic Schema (The Blueprint)
class Student(BaseModel):
    name: str
    email: EmailStr
    age: int

# ==========================================
# PART 1: DESERIALIZATION (Unpacking Data)
# ==========================================
# Imagine this RAW JSON (text string) arrived from Postman or a frontend client:
incoming_json_data = '{"name": "Rahul", "email": "rahul@example.com", "age": "22"}'

print("--- 1. Raw Incoming Data (JSON String) ---")
print(type(incoming_json_data))  # This is just a plain String (text)
print(incoming_json_data)       # This is the raw data we received from Postman

# Using Pydantic to convert this text string into a live Python Object.
# This process is called 'Deserialization' (Validation happens automatically here).
student_object = Student.model_validate_json(incoming_json_data)

print("\n--- 2. After Deserialization (Pydantic Object) ---")
print(type(student_object))
print(f"Student Name: {student_object.name}")  # We can now use dot notation (.name)
print(f"Age (Automatically converted from string '22' to integer {type(student_object.age)}): {student_object.age}")


# ==========================================
# PART 2: SERIALIZATION (Packing Data)
# ==========================================
# Now imagine we want to send this validated object back over the internet or save it.
# To do this, we turn the Python object back into a raw JSON string.
# This process is called 'Serialization'.

serialized_data = student_object.model_dump_json()

print("\n--- 3. After Serialization (Back to JSON String) ---")
print(type(serialized_data))  # This converts it back into a standard string class
print(serialized_data)       # This data is now perfectly packed and ready for transit!
