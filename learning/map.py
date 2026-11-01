letter = ['a','b','c']
# cap = []
# for l in letter:
#     cap.append(l.upper())

# print(cap)

# same thing could be done using the map(function,iterable) iterator

print(list(map(str.upper,letter)))

num = ['1','2','3']
print(list(map(int,num)))
