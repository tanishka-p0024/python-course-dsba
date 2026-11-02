n = int(input("Number of items you would like to check: "))
user_defined_list = []
for l in range(n):
    item = input('What are your elements: ')
    user_defined_list.append(item)

unique = []
duplicate = []

for i in user_defined_list:
    if i in unique:
        duplicate.append(i)
    else:
        unique.append(i)

print(duplicate)
print(unique)