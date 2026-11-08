s = "*"
n = int(input('What n do you want to use?'))
for row in range(1,n+1):
    for star in range(1,row+1):
        print(s,end='')
    print()

# Normally python's print() functions ends in new line by default,
#We want stars in a row to be printed side by side 
# The second print adds a new line in a row
