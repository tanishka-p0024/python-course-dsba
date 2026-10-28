import random
computer = random.randint(1,100)

while True:
    user = int(input('Enter your guess what number it could be: '))
    if user<computer:
        print('too low')
    elif user>computer:
        print('Too high')
    else:
        break

print("You guessed it!")
    


