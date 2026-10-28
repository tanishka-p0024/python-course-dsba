'''Write a program that acts as a maths trainer:
Typing x stops the program and prints the score.'''


import random

cor=0
wrg=0
while True:
    a = random.randint(1,100)
    b = random.randint(1,100)
    ops = ['*','+','-']
    c = random.choice(ops)

    if c == '*':
        r = a*b
    elif c == '+':
        r = a+b
    elif c == '-':
        r = a-b
    
    user = input(f'What is {a} {c} {b} = ')

    if user == 'x':
        total = cor + wrg
        break

    user = int(user)

    if user==r:
        print('Thats correct !')
        cor = cor + 1
    elif user != r:
        print('Thats wrong')
        wrg = wrg + 1
    
    
    
        
print(f'You got {cor} correct out of {total} asked')