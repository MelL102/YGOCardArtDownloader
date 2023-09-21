import urllib, json
from urllib.request import urlopen
import requests
import shutil
import os
import pathlib
import time

response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")

response_json = json.loads(response.text)


def getCardImageURL(response_json):
    return response_json["image_url_cropped"]


def getCardName(response_json):
    invalid = '/[/\\?%*:|"<>]/'
    card_name = response_json["name"]
    for char in invalid:
        card_name = card_name.replace(char, "")
    return card_name


def getLenght(response_json):
    return len(response_json["data"])


def downloadCardImage(response_json):
    card_name = "Error! Card name could not be found"
    folder = "CardArt"
    if not os.path.exists(folder):
        os.makedirs(folder)

    os.chdir(folder)

    for x in response_json["data"]:
        for i, y in enumerate(x["card_images"]):
            try:
                image_source = getCardImageURL(y)
                card_name = getCardName(x)
                urllib.request.urlretrieve(image_source, card_name + "_" + str(i) + ".jpg")
            except:
                print("Image for: " + card_name + " could not be found")
            time.sleep(0.1)


downloadCardImage(response_json)
