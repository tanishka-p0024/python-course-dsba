'''Write a program that prints the multiplication table from 1 to 10 for some integer 𝑛.
Then extend it to quiz a student: ask how much 𝑝 × 𝑛 is, or which 𝑝 satisfies 𝑛 × 𝑝 = 𝑟 
for a given result 𝑟.'''

import random
p = random.randint(1,10)
n = int(input("What Table you know : "))
r = p*n

print(f'What is {n}x{p}?')
answer = int(input(f'{n} x {p} is: '))
if answer  == r:
    print('Youre right!')
else:
    print('Youre wrong')