import requests

params = {"q": "pizza"}  # the url uses q is for searching
r = requests.get("http://www.google.com/search", params = params)  # request a page, with a GET variable
print("Satus:", r.status_code)  # 200 = success, search HTTP status codes

print(r.url)  # requested url, 'google.com'
print(r.text)  # html codes

file = open("./page.html", "w+")
file.write(r.text)  # saving all the html source code in file/ saving the requested url page

