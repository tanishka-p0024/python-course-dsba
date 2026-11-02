'''Given a list, remove the duplicates, 
and separately find which elements were duplicated.
Do it with a set and without. What does the set buy you, 
and what does it cost you? (Think about order, and
about what a set requires of its elements.)'''

# USING SET

n = int(input("Number of items you would like to check: "))
user_defined_list = []
for l in range(n):
    item = input('What are your elements: ')
    user_defined_list.append(item)

unique_set = set()
for i in user_defined_list:
    unique_set.add(i)

# print(unique_set)


unique_set1 = set()
duplicates = set()

for item in user_defined_list:
    if item in unique_set1:
        duplicates.add(item)
    else:
        unique_set1.add(item)

