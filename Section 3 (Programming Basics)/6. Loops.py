

# for loops:
numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

names = ["Muiz", "Sakib", "Fahad"]
for person in names:
    print("This is " + person)


# while loops:
run = True
current = 1

while run:
    if current==100:
        run = False

    else:
        print(current)
        current+=1
