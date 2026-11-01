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
z = str(input('What operation would u like to perform-+, -, *, /: '))


# Function can acts as variables too
operations = {
    "+": add,
    "-": diff,
    "*": mul,
    "/": div
}

print(operations[z](a,b))