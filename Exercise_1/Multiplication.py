'''Write a program that prints the multiplication table from 1 to 10 for some integer '''

n = int(input('Enter the input '))
for i in range(1,11):
    r = n*i
    print(f'{n} x {i} = {r}')

