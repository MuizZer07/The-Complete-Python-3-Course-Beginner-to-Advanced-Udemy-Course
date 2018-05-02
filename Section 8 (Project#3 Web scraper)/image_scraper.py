# image scraper
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os

def start_search():

    search = input("Search for:")
    n = int(input("How many Images you want to download: "))

    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()

    dir_name = os.path.join("./scraped_images/", dir_name)
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/images/search", params = params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    i = 0
    for item in links:
        if(i>=n):
            break
        try:
            img_obj = requests.get(item.attrs["href"])  # getting the image
            print("Getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]  # extracting title from the link
            try:
                img = Image.open(BytesIO(img_obj.content))  # creating an image object
                img.save("./" + dir_name + "/" + title, img.format)  # saving in a new directory
                print("Downloaded Successfully!")
            except:
                print("Could not save the image.")
        except:
            print("could not request image.")

        i += 1
    start_search()

start_search()