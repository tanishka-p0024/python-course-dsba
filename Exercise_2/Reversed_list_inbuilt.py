n = int(input('How many items would you like to insert: '))
user_defined_list = []
for i in range(n):
    item = input('What is your item: ')
    user_defined_list.append(item)

print(f'The reversed list of {user_defined_list} is {list(reversed(user_defined_list))}')