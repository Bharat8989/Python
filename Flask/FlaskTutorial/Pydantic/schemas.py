from pydantic import BaseModel, EmailStr, Field

class UserRegisterSchema(BaseModel):
    # Enforce minimum and maximum lengths for safety
    username: str = Field(min_length=3, max_length=100)
    email: EmailStr  # Automatically validates correct email syntax (@, domain, etc.)
    mobile_number: str = Field(min_length=10, max_length=15)
    password: str = Field(min_length=8, max_length=255) # Enforces a strong length

    # Configuration to read standard database objects if needed
    class Config:
        from_attributes = True
