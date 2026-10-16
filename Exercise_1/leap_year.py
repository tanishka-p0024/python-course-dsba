a = int(input('Enter the year you wanna check'))

if a%400 == 0:
    print(f'The year {a} is a leap year')
elif a%400 !=0 and a%100==0:
    print(f'The year {a} is not a leap year')
elif a%400 !=0 and a%4==0 and a%100!=100:
    print(f'The year {a} is a leap year')
else:
    print('Not a leap year')