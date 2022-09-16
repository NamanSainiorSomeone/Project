while True:
   name = input("Whtas your name: ")
   if name != "" :
        print(name)
        break

username = input("Write your usernsme: ")
for i in username:
    if i == " ":
        continue
    print(i,end = "")

print()
password = input("Write your password: ")
for i in password:
    if i== "!" or i== "$" or i =="*":
        pass
    print(password,end="")