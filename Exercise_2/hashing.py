'''
Write a function that turns a sentence into a hashtag: capitalise every word, remove the spaces, concatenate,
and prepend a #'''
n = str(input('Write your word to make it hashtag: '))
def hashing(word):
    word = word.title()
    word = word.replace(' ','')

    return "#" + word
print(hashing())

# Learned the difference between the capitalize and title 
# Capitalize just make first word capital
# Title makes every word capital.


    
