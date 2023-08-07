import cv2

def read_image(image_path):
    return cv2.imread(image_path)

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def extract_channels(image):
    blue, green, red = cv2.split(image)
    return blue, green, red

def crop_image(image, x, y, width, height):
    return image[y:y+height, x:x+width]



