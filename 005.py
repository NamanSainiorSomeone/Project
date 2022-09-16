rows = int(input("how many rowss do you want?"))
columes = int(input("how many columes do you want?"))
symbole = input("write your symbole")

for i in range(rows):
    for j in range(columes):
        print(symbole, end = "")
    print()