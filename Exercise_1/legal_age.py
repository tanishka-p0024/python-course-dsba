a = str(input('Enter the country-uk/us/de '))
b = int(input('Enter the age '))
if a == 'uk':
    if b >=18:
        print('Youre legally allowed to drink')
    else:
        print('Not legal')
elif a == 'us':
    if b>=21:
        print('Youre legally allowed to drink')
    else:
        print('Not legal')
elif a == 'de':
    if b>=16:
        print('Youre legally allowed to drink')
    else:
        print('Not legal')
