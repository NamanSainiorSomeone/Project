def hello(name, last):
    print("Hello "+name +" "+last)
    

name=input("whats your name: ")

if name != None:
    print(hello(name, "saini"))

hello(last="saini", name=name)