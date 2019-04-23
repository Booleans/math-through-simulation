# You have a shuffled deck of 60 cards containing the following cards of special interest.
# Three of these cards in the deck are marked with a diamond.
# Three of the cards are marked with a star.
# The remaining cards are nothing special. 
# You draw an initial hand of five cards, after which you must discard any of the star cards for
# an additional three cards drawn from the top of the deck. This process is repeated until you
# find yourself with a hand that does not contain any star cards. 
# Write a simulation to approximate the probability that your initial draw results in a final hand containing a diamond card.

import random
n_sims = 10**5
# Success is defined as an ending hand with a diamond card.
n_success = 0

for _ in range(n_sims):
    # D for diamond, S for star, X for all other cards.
    deck = ['D']*3 + ['S']*3 + ['X']*54
    random.shuffle(deck)
    hand = []
    # Create the initial hand.
    for i in range(5):
        hand.append(deck.pop())
    # If there is a diamond in our initial hand we know we end up with one in the final hand.
    if 'D' in hand:
        n_success += 1
        continue

    while 'S' in hand:
        hand.remove('S')
        for _ in range(3):
            hand.append(deck.pop())

    if 'D' in hand:
        n_success += 1

print(n_success/n_sims)