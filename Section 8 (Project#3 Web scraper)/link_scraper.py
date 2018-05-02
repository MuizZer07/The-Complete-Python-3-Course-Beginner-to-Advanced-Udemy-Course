# normal link scraper
from bs4 import BeautifulSoup
import requests

search = input("Enter search term: ")
params = {"q" : search}
r = requests.get("http://www.bing.com/search", params = params)

# parse html contents of the requested page and turning into BeautifulSoup Object
soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify()) # prints out all the html contents
results = soup.find("ol", {"id": "b_results"})  # finding the 'ol's from the html which has a 'id': b_results
links = results.findAll("li", {"class": "b_algo"})
# kind of filtering the whole html content and savinf in a list of content that we want

for item in links:
    item_text = item.find("a").text  # extracting text from all the links in the list
    item_href = item.find("a").attrs["href"]  # extracting links, .attrs specifies special attributes
    item_summary = item.find("a").parent.parent.find("p").text  # parent content in the html of the selected item

    if item_text and item_href:  # if there is a link and it has text(Title)
        print(item_text)
        print(item_href)
        print(item_summary)


