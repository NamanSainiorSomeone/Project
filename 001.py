import math


name = "naman"
name2 = "saini"
age = '17'#string
names = name + " "+ name2
print (type(name))
print (names + " is " + age)


age2 = 15
print (age2)
age2 = age2 + 1
print (age2)
age2 += 1
print (age2)
print ('you are '+ str(age2))


height = 249.5261
print ("Height is " + str(height) + "   "+ str(type(height)))


human = False
if human == True:
    print("Human")
if human == False:
    print("Alien")


I , double , stringg , boolian = 1 , 1.0 , "one" , True
print (I)
print(double)
print (stringg)
print (boolian)


names = "naman Saini"
print (len(names))
print (names.find("S"))
print (names.capitalize())
print (names.lower())
print (names.upper())
print (names.isdigit())
print (names.isalpha()) #coz of space
print (names.count("n"))
print (names.replace("n" , "m"))
print (names*2)

x = 1.0

print(int(x))

x = int(x)
print (x)
y = "10"
y = int(y)
print (y*3)


#what = input("whats your name? ")
#print ("Your name is: "+ what)# input is always str
#ages = int(input("Your age? "))
#print (ages + 1)


pi = -3.14
print (round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(653))
x= 1
y= 100
z= 282745
print (max(pi,z,x,y))
print (min(pi,z,x,y))

       # 01345
naame = "naman saini"
first_name= naame[0]
print (first_name)
first_name= naame[:5]#nothing before : is 0         #stoping index(5) is exclusive
print (first_name)
last_name = naame[6:]
print(last_name)
funky = naame[::2]  #prints every 2nd char
print(funky)
reversed_name = naame[::-1]
print(reversed_name)


website = "https://www.google.com/"
slice = slice(12,-5) #-ve starts from -1 adn is exclusive
print(website[slice])