from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import io # for creating in memory stream and sending binary object
import cv2 # for imencode and [1] for binary data and tobytes() for converting to bytes

# for sending a stream response
from starlette.responses import StreamingResponse 
from image_processing import read_image, convert_to_grayscale, extract_channels, crop_image

import shutil
import random

app = FastAPI()

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

            # for sending html response
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
    <head>
        <title>Image Processing with OpenCv</title>
        <style> 
            img {
                width:200px; 
                height: auto;
            }
        </style>
    </head>
    <body>
        <h1>Image Processing with OpenCv</h1>
        <img src="/grayscale" />
        <img src="/blue_channel" />
        <img src="/green_channel" />
        <img src="/red_channel" />
        <img src="/cropped" />
    </body>
    </html>
    """

# image = read_image("eye-1.jpg")


def res(img):
    return StreamingResponse(
        io.BytesIO(cv2.imencode(".jpg", img)[1].tobytes()), 
        media_type="image/jpg"
    )

 
@app.post('/get-diagnosis')
def get_diagnosis(image: UploadFile = File(...)):
    # Save the uploaded image to the "static" folder
    # file_location = f"static/{image.filename}"
    # with open(file_location, "wb") as f:
    #     shutil.copyfileobj(image.file, f)
    states = ['Normal','Abnormal']
    return {
        "filename": image.filename,
        "info" : random.choice(states)
    } 

@app.post("/get-images")
def get_images(image : UploadFile = File(...)):
    grayscale_image = "" # convert_to_grayscale(image)
    b,g,r = "" #extract_channels(image)
    cropped_image = crop_image(image, x=300, y=100, width=200, height=200)
    images = [
        res(grayscale_image),
        res(b),
        res(g), 
        res(r),
        res(cropped_image)
    ] 
    return {
        "images": images
    }










# @app.get("/grayscale")
# def get_grayscale_image():
#     grayscale_image = convert_to_grayscale(image)
#     return res(grayscale_image)

# @app.get("/blue_channel")
# def get_blue_channel():
#     blue, _, _ = extract_channels(image)
#     return res(blue)

# @app.get("/green_channel")
# def get_green_channel():
#     _, green, _ = extract_channels(image)
#     return res(green)

# @app.get("/red_channel")
# def get_red_channel():
#     _, _, red = extract_channels(image)
#     return res(red)

# @app.get("/cropped")
# def get_cropped_image():
#     cropped_image = crop_image(image, x=300, y=100, width=200, height=200)
#     return res(cropped_image)
