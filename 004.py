import time
name = ""

while name=="":
    name =str(input("whats your name? "))
print("hi "+ name)


for i in range(10,0,-1):
    print(i)
    time.sleep(1)

print ("happy birthday "+ name)