'''Given a list, produce the reversed list.
Do it at least three ways: with an explicit loop, with slicing, and with a built-in. Which of them modify the original
list, and which return a new one? Check with id()'''

# Letting user input their own list
user_defined_list = []
n = int(input('How many items would you like to input'))
for i in range(n):
    item = input('What are your inputs: ')
    user_defined_list.append(item)

# print(user_defined_list)
reversed_list = []
for r in range(len(user_defined_list)-1,-1,-1):
    last_item = user_defined_list[r]
    reversed_list.append(last_item)

print(reversed_list)

