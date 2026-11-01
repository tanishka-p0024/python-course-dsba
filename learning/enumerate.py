l = ['a','b','c']
# using enumerate gives us indexing 
print(list(enumerate(l)))
print(list(enumerate(l,start=1)))

for index,value in enumerate(l):
    print(index,value)

