import requests

# POST methods, posting data to the url, sending data to POST forms
data = {
    "name": "Muiz Ahmed Khan",
    "email": "muiz@muiz.com"
}  # variable names are found in html file

url = "https://www.w3schools.com/php/welcome.php"
r = requests.post(url, data)

file = open("newfile.html", "w+")
file.write(r.text)