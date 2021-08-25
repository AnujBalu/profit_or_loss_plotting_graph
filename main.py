import matplotlib.pyplot as plt
import json
#import user_input
import file
import os

#money_got = user_input.graph.salary_got('self')
#print(money_got)
step = 0
info = []
text = open('detail1.dat','r')
text_loaded = json.loads(text.read())
for text in text_loaded:
    info.append(text)
print(info)
while step != 'x':
    step = int(input("Enter a number: "))
    if step == 1:
        info.append(file.create_file())
        print(info)
    elif step == 2:
        file.save_file(info)
        #print(type(save))
    elif step == 3:
        print(file.find_file(info,name ='anuj'))
plt.plot(money_got)


plt.show()