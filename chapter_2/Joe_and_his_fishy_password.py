name = ''
password = ''
while True:
    print("What's your name :")
    name = input()
    if name != "Joe":
        continue
    print("hello Joe, what's your password? (Hint: its a fish)")
    password = input()
    if password == 'shark':
        break
print("access granted")
