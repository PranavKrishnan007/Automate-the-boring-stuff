cats = []
while True:
    print("Enter the name of the cat " + str(len(cats)+ 1 ) + " : ")
    name = input()
    if name == '':
        break
    cats.append(name)
print("the names of the cats are : ")
for x in cats:
    print(x)
