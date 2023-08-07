from fastapi import FastAPI , Body , Depends
from app.schema import PostSchema , UserSchema , UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwt_bearer


app = FastAPI()

users = []

posts = [
    {
        "id": 1,
        "title": "First post",
        "content": "This is the first post"
    },
    {
        "id": 2,
        "title": "Second post",
        "content": "This is the second post"
    },
    {
        "id": 3,
        "title": "Third post",
        "content": "This is the third post"
    }
]


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts/get/{id}")
async def get_post(id: int):
    for post in posts:
        if post["id"] == id:
            return {
                "post": post
            }
    return {
        "Error" : "can\'t find posts with id : " + str(id)
    }

@app.post("/posts/create", dependencies=[Depends(jwt_bearer())])
async def create_post(post: PostSchema):
    for item in posts:
        if item["id"] == post.id:
            return {
                "Error": "Post already exists with id : " + str(post.id)
            }
    posts.append(post.dict())
    return {
        "success" : "Post added succesfully",
        "post": post
    }


@app.post("/users/sign-up")
async def sign_up(user: UserSchema = Body(default=None)):
    users.append(user.dict())
    return signJWT(user.email)


@app.post("/users/login")
async def login(user: UserLoginSchema = Body(default=None)):
    if validate_user(user):
        return signJWT(user.email)
    return {
        "Error" : "Invalid credentials"
    }

def validate_user(data : UserLoginSchema):
    for user in users:
        if user["email"] == data.email and user["password"] == data.password:
            return True
    return False