import matplotlib.pyplot as plt
import json
import file

info = []
try:
    text = open('detail1.dat','r')
    text_loaded = json.loads(text.read())
    for text in text_loaded:
        info.append(text)
except:
    print("file is empty....")
    print("please load your information")
while True:
    try:
        step = int(input("Enter a number: "))
        if step == 1:
            info.append(file.create_file())
        elif step == 2:
            file.save_file(info)

        elif step == 3:
            file.find_file()
    except:
        print("Check the number you entered")

