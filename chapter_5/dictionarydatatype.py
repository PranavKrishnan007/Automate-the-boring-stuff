birthdays = {'Alice' : '1st jan', 'Bob' : '1st april'}

while True:
    print('Enter a name to check the birthday : ')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('This name does not exist in the database! ')
        print('what is their birthday?')
        birth = input()
        birthdays[name] = birth
        print('database updated!')
