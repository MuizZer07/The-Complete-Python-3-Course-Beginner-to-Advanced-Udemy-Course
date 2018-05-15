import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher


class Commander:
    def __init__(self):
        self.exit = ["quit", "goodbye", "exit", "bye"]
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "cancel", "negative", "don't", "wait"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("You haven't told your name is..")
            else:
                self.respond("My name is PyBot.")
        else:
            f = Fetcher("https://www.google.co.uk/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)

    def respond(self, response):
        newfile = open("k.txt", "w+")
        newfile.write(response)
        newfile.flush()
        subprocess.call('ptts -u "k.txt"', shell=True)
