
from pydantic import BaseModel, field_validator, model_validator

class CreateUser(BaseModel):
    email: str
    password: str
    confirm_password: str

    @field_validator("email")
    def validate_email(cls, value):

        if "admin" in value:
            raise ValueError("This mail is not allowed")
        return value
    
    # @field_validator("confirm_password")
    # def password_match(cls, v, values, **kwargs):
    #     if values.data['password'] != v:
    #         raise ValueError("Password doesn't match!")
        
    #     return v
    
    @model_validator(mode="before")
    def password_match(cls, values):
        if values.get("password") != values.get("confirm_password"):
            raise ValueError("Both the passwords should match!")
        
        return values
    
    
    
    # @field_validator("password", "confirm_password")
    # @classmethod
    # def validate_password(cls, value, field):

    #     pwd = ""
    #     if field.name == "password":
    #         pwd = value
    #     if field.name == "confirm_password" and pwd != value:
    #         raise ValueError("Please validate the password")
    #     return value
     
    
first_user = CreateUser(email="admime@gmail.com",
                        password="My secret",
                        confirm_password= "My secrets")
print(first_user)
