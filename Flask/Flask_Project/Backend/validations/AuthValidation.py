from marshmallow import Schema, fields, validate 

class RegistrationUser(Schema):
    username = fields.String(
        required=True, 
        error_messages={'required': 'Username is required'}
    )
    email = fields.Email(
        required=True, 
        error_messages={
            'required': 'Email is required',
            'invalid': 'Invalid email address'
        }
    )
    password = fields.String(
        required=True, 
        validate=[
            validate.Length(
                min=6, 
                max=20, 
                error='Password must be between 6 and 20 characters long'
            ),    
            validate.Regexp(
                r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,20}$',
                error='Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character'
            )
        ],  
        error_messages={'required': 'Password is required'}
    )
    
# class LoginUser(Schema):
#     # Minimal fields for basic authentication
#     email = fields.Email(
#         required=True, 
#         error_messages={
#             'required': 'Email is required',
#             'invalid': 'Invalid email address'
#         }
#     )
#     password = fields.String(
#         required=True, 
#         error_messages={'required': 'Password is required'}
#     )
    
register_user_schema = RegistrationUser()
# login_user_schema = LoginUser()
