# creating a file variable to write
newfile = open("newfile.txt", "w+")  # 'w' is writing mode

string = "ABCDEFGHIJKLMNOPQRSTUVWZ"
# writing the string in the text file
newfile.write(string)