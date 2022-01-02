while True:
    print("ENTER YOUR AGE: ")
    age = input()
    try:
        age = int(age)
    except:
        print("KINDLY USE NUMERIC DIGITS FOR AGE: ")
        continue
    if age < 1:
        print("PLEASE ENTER A POSITIVE NUMBER FOR AGE: ")
        continue
    break

print(f'Your age is {age}.')
