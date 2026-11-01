# Zip combines 2 or more sequences into pairs i.e tuples
l = ['a','b','c']
num = [1,2,3]
print(list(zip(l,num)))

# Now for iterating:
for l,n in zip(l,num):
    print(l,n)