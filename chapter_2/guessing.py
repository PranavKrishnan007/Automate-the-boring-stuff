import random
num = random.randint(1,20)
print("I am thinking of a number between 1 and 20 ")
for guess in range(1, 7 ):
    guessing = int(input())
    if guessing > num:
        print("Too high")
    elif guessing <num:
        print("Too low")
    else:
        break
if guessing == num :
    print("yup thats the number I was thinking of")
else:
    print("nope I was thinking of " + str(num) + ".")
