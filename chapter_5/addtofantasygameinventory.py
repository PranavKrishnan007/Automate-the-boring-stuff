def printinventory(stuff):
    print("Inventory:")
    sum = 0
    for k,v in stuff.items():
        print(v,k)
        sum += v
    print("Total number of items :", sum)

inv = {'gold coin': 45, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] 
for x in dragonLoot:
        inv.setdefault(x, 1)
printinventory(inv)
