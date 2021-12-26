inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def printinventory(stuff):
    print("Inventory:")
    sum = 0
    for k,v in inventory.items():
        print(v,k)
        sum += v
    print("Total number of items :", sum)

printinventory(inventory)
