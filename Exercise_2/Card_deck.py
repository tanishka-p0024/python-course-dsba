suits = ['♤','♥','♦','♧']
ranks = ['A','2','3','4','5','6','7','8','9','10',
         'J','K','Q']
deck = []
for r in ranks:
    for s in suits:
        card = r + s
        deck.append(card)
# print(deck)

import random
shuffled_deck = random.shuffle(deck)
player_one = shuffled_deck[0:12]
player_two = shuffled_deck[13:25]
player_three = shuffled_deck[26:38]
player_four = shuffled_deck[39:51]

