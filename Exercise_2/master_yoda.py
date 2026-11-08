'''
Given a sentence, return it with the words reversed.'''

sentence = str(input('Enter the sentence to reverese it: '))
list_word = []
for i in sentence.split():
    list_word.append(i)

rev_list = list(reversed(list_word))
rev_sentence = ''
for i in rev_list:
    rev_sentence = rev_sentence+ i + " "

print(rev_sentence)

