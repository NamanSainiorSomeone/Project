
bartan = {"katori","plate","ggg","chamach","chamach","chamach"}
bartan.add("any")
bartan.remove("any")
#bartan.clear()

name = {"tr4s","ygtd","hvt","ggg"}

bartan.update(name)
for x in bartan:
    print(x)
print(bartan.difference(name))