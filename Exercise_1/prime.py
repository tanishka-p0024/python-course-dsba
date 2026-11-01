n = int(input('Enter your number: '))
if n <= 1:
    print('no')
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print('yes')
    else:
        print('no')