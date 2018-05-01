import requests
from io import BytesIO  # used for Byte data
from PIL import Image

url = "https://wallpapercave.com/wp/Yr78gtw.jpg"

r = requests.get(url)  # an image address/url
print("Status code:", r.status_code)  # getting status code

image = Image.open(BytesIO(r.content))  # creating a Image object from the Byte data retrieced from the url content

print(image.size, image.format, image.mode)  # size, format and image mode //(1920, 1200) JPEG RGB
path = "./image." + image.format

# saving the image object as the original format
try:
    image.save(path, image.format)
except IOError:
    print("Can not save the image.")


