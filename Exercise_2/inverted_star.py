s = '*'
n = int(input('How many rows would u like to print? '))

for row in range(1,n+1):
    for star in range(n-row+1):
        print(s,end='')
    print()