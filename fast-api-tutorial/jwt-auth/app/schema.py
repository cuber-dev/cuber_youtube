

from pydantic import BaseModel , Field, EmailStr


class PostSchema(BaseModel):
    id : int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)
    class Config:
        json_schema_extra = {
            "post_demo":{
                "title":"some title",
                "content":"some content"
            }
        }


class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None) 
    class Config:
        json_schema_extra = {
            "user_demo":{
                "name" : "someone",
                "email":"someone@example.com",
                "password":"pass123"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None) 
    class Config:
        json_schema_extra = {
            "user_demo":{
                "email":"someone@example.com",
                "password":"pass123"
            }
        }