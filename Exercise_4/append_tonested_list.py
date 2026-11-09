'''
Write a function that appends a new value 
to every inner list of a nested list.
Now answer, before running anything: is nested_list itself modified? 
Then write a version that leaves the
argument untouched, and prove with id() that it does'''
nested_list = [[1, 2], [3, 4], [5]]

# for inner_list in nested_list:
#     inner_list.append('new')
# print(nested_list)
# Yes indeed the nested list is modified


import copy
b = copy.deepcopy(nested_list)
for inner_list in b:
    inner_list.append('new')

print(b)
print(nested_list)
print(id(nested_list))
print(id(b))

print(id(nested_list[0]))
print(id(b[0]))