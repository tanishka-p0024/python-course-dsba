def master_yoda(sentence):
    words = sentence.split()
    # split already creates a list lol
    '''With slicing'''
    # words[::-1]
    '''With built in function'''
    rev_words = list(reversed(words))
    reversed_sentence = ' '.join(rev_words)

    return reversed_sentence

print(master_yoda('Good morning this is such a lovely morning'))