# Letting user input their list
n = int(input('How many items would you like to insert: '))
user_defined_list = []
for i in range(n):
    item = input('What is your item: ')
    user_defined_list.append(item)
# Reversing using slicing
# A = [2,3,4]
# B = A[::-1]
# print(B)
print(f'Your given list {user_defined_list}')
reversed_list = user_defined_list[::-1]
print(f'Your reversed list {reversed_list}')

