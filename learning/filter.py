# filter(function,iterable)
letters = ['a','','b','c',None,False]

# None/bool : removes all falsy values like empty strings, none false ,etc
print(list(filter(None,letters)))

# isalpha - keeps only alphabetic terms 
l = ['a','123','42','hello']
print(list(filter(str.isalpha,l)))