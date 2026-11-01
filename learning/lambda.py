#output =  lambda input: Expression
'''Lambda acts as a function same as def XX()'''

# For one input
'''multiple = lambda x:x*2
print(multiple(2))'''

# For multiple input
'''add = lambda x,y : x+y
print(add(4,5))

check = lambda i:i in "python"
print(check('u'))
'''
# Using map(function,iterable) with lambda

prices = ['$12.99','$5.40','$80.00']
print(list(map(lambda p :float(p.replace('$','')),prices)))

# p = '$12.99'
# float(p.replace('$',''))