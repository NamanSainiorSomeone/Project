from genericpath import isdir
import os
path = "D:\\Coading\\test.txt"

if os.path.exists(path):
    print("yes")
    if os.path.isfile(path):
        print("file")
    elif os.path.isdir:
        print("dir")
    
else:
    print("no")








try:
    with open('tesdt.txt') as file:
        print(file.read())
        print(file.closed)

except FileNotFoundError:
    print("no file")


#writing




text = 'hmmmmmmmm hmhmhmhmhmhmmh\n hbhbhb'
with open('text1.txt','w')as file:
    file.write(text)