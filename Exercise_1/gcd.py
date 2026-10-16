a = int(input('Enter the first no '))
b = int(input('Enter the second no '))
d = min(a,b)
while a%d!=0 or b%d!=0:
    d = d-1

print(f'The GCD of {a} and {b} is {d}')
