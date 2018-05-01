import simplejson as json  # 'as' keyword renames the module we import
import os

# checking if the file does exist and the file size is not zero
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")  # opening the existing file in 'read-write' mode
    data = json.loads(old_file.read())  # retrieving string from json object and loaded into a python object
    print("Current age is", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1  # increasing the age in the python object
    print("New age is", data["age"])
else:
    old_file = open("./ages.json", "w+")  # creating a new file in write mode if there is no file exists in such name
    data = {
        "name":"Muiz",
        "age": 23
    }  # creating a python object
    print("No file found, setting default age to", data["age"])

old_file.seek(0)  # setting the cursor at the beginning, position 0 in the file
old_file.write(json.dumps(data))  # dumping in the python object, converting into a json object
