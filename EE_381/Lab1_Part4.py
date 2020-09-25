import random

N = 1000000
hits = 0

for j in range(N):
    hand = []
    deck = []
    #creates a deck
    for i in range(52):
        deck.append(i+1)
    #choosing 6 cards
    while(len(hand) < 6):
        card = random.randint(1,52)
        #if the card has been chosen,
        #chooses another card
        #if not, adds to hand
        if(deck.__contains__(card)):
            hand.append(card)
            deck.remove(card)

    #converting numbers to corresponding cards
    for i in range(6):
        hand[i] = hand[i]%13

    #counting number of four of kinds
    for i in hand:
        if(hand.count(i)==4):
            hits+=1
            break
print("The probability of getting four of a kind in 1000000 tries is",hits/N)





