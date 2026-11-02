'''A string is a palindrome if it reads the same forward and backward: 
”anna”, ”civic”, ”level”, ”hannah”. Write a program that reads 
a string and uses a loop to determine whether it is a palindrome. 
Display a meaningful message.
Then handle ”A man, a plan, a canal: Panama” – 
ignore case, spaces and punctuation.'''

word = str(input('Enter the word to check if its palindrome or not : '))
word = word.lower()
word = word.replace(' ','')
word = word.replace(',','')
word = word.replace(':','')
if word == word[::-1]:
    print(f'{word} is a palindrome')
else:
    print('Its not a palindrome')
