'''Write a program that asks for two numbers, 
then for the operation to apply, then performs it and 
prints the result. Write one function per operation (+, -, *, /).
Once it works: store the four functions in a dictionary keyed 
by the operator symbol, and replace the if/elif chain
with a single lookup. Functions are values like any other.'''

def add(x,y):
    return x + y
def diff(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

a = int(input('What is your first number'))
b = int(input('What is your second number'))
z = str(input('What operation would u like to perform-+, -, *, /: ' ))
if z == '+':
    print(add(a,b))
elif z == '-':
    print(diff(a,b))
elif z == '*':
    print(mul(a,b))
elif z == '/':
    print(div(a,b))



