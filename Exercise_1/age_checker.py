a = int(input('Enter the age to know the category '))
if a in range(0,13):
    print('Kid')
elif a in range(13,20):
    print('Teenager')
elif a in range(20,31):
    print('Young Adult')
elif a in range(31,65):
    print('Adult')
elif a>=65:
    print('Senior')
else:
    print('Age is invalid, please enter +ve or integers')