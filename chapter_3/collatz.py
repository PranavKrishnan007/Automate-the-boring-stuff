def collatz(number):
    if number % 2 == 0:
        out = number // 2
        print(out)
        return(out)
    else:
        out = 3 * number + 1
        print(out)
        return(out)

num = input()
num = int(num)
value = collatz(num)
while True:
    if value == 1:
        exit
    else:
        value = collatz(value)
        
print("Hurray done!")
