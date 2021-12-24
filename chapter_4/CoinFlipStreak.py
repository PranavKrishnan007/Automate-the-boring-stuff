import random
numberOfStreaks = 0
values = []
for experimentNumber in range(10000):
    # Code that creates a list of 10000 'heads' or 'tails' values.
    a = random.randint(0,1)
    values.append(a)
# Code that checks if there is a streak of 6 heads or tails in a row.
for x in range(len(values)-5):
    if values[x] == values[x+1] == values[x+2] == values[x+3] == values[x+4] == values[x+5]:
        numberOfStreaks += 1
print(numberOfStreaks) 
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
