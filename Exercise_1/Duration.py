'''Write a program that reads a duration as hours, minutes and seconds,
 then displays the total number of seconds.'''

a = int(input('Whats the HH'))
b = int(input('Whats the MM'))
c = int(input('Whats the SS'))

seconds = 3600*a + 60*b + c
print(f'The total seconds has been {seconds}')


