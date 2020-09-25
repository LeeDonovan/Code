import numpy as np
import matplotlib.pyplot as plt
import random

################### Part 1 #########################################################
def partOne():
    N=100000
    max_rolls = 60
    results = np.zeros((N, 1))#array of zeroes but will change if sum equals to 7
    for i in range(N):
        d1=np.zeros((max_rolls, 1))
        d2=np.zeros((max_rolls, 1))
        
        for j in range(max_rolls):
            d1[j, :] = random.randint(1,6)#1-6 random nums
            d2[j, :] = random.randint(1,6)
        sum = d1 + d2#added to check for 7
        counter = 0
        while counter < len(sum):
            if sum[counter][0] == 7:
                results[i] = counter
                break
            counter+=1
    b = range(0,60)
    sb = np.size(b)
    h1, binedges = np.histogram(results, bins = b)
    b1 = binedges[0:sb-1]
    fig1=plt.figure(1)
    plt.stem(b1,h1)
    plt.title('Stem plot - Number Of Rolls for a Sum Of 7')
    plt.xlabel('Number Of Rolls')
    plt.ylabel('Number of occurrences')
    fig1.savefig('Sum of Two Dices Equal to Seven.jpg')

    fig2=plt.figure(2)
    p1=h1/N
    print(p1[0])#0.16615
    print(p1[1])#0.1407
    plt.stem(b1,p1)
    plt.title('Stem plot - Number Of Rolls for a Sum Of 7: Probability mass function')
    plt.xlabel('Number Of Rolls')
    plt.ylabel('Number of occurrences')
    fig2.savefig('PMF of Sum Of 7.jpg')

    plt.show()

########################### Part 2 ##########################################################

def partTwo():
    N = 10000

    die = [1,2,3,4,5,6]#die sides
    results = np.zeros((6,),dtype=int)
    p1 = 0.1
    p2 = 0.15
    p3 = 0.3
    p4 = 0.25
    p5 = 0.05
    p6 = 0.15
    prob =[p1,p2,p3,p4,p5,p6]#die weights
    while N > 0:
        choice = random.choices(die, weights = prob)
        #sets the weight of each position from die of being chosen
        
        if choice[0] == die[0]:
            results[0]+=1
            
        if choice[0] == die[1]:
            results[1]+=1

        if choice[0] == die[2]:
            results[2]+=1

        if choice[0] == die[3]:
            results[3]+=1

        if choice[0] == die[4]:
            results[4]+=1

        if choice[0] == die[5]:
            results[5]+=1
        N-=1
    results = (results / 10000 )#percentage
    #b = range(1,7)
    # sb = np.size(b)
    # h1, binedges = np.histogram(results, bins = b)
    # b1 = binedges[0:sb-1]
    # print (results)
    # plt.stem(b1,h1)
    # p1 = h1/N
    #result = results/N
    plt.stem(range(1,7),results)
    #fig1 = plt.figure(1)
    plt.title('Stem Plot - Unfair Die Results - PMF')
    plt.xlabel('Die Number')
    plt.ylabel('Probability of tosses')
    #fig1.savefig('example.jpg')

    plt.show()

########################## Part 3 ##########################################################################

def partThree():
    N = 100000
    num_experiments = 100000
    counter_heads=0
    while num_experiments > 0:#run 100,000 times
        num_coins = 100
        heads = 0
        tails = 0
        while num_coins > 0:#flip 100 coins
            coin_side = random.randint(1,2)
            if coin_side == 1:
                heads+=1#heads
            if coin_side == 2:
                tails+=1#tails
            num_coins-=1
        if heads == 35:#check for 35 heads in a run
            counter_heads+=1
        num_experiments-=1
    print("Number of 35 heads: ", counter_heads)
    print("Chance of 35 heads out of ", N, " would be : " , counter_heads/N)

######################## Part 4 ##################################################

def C(n,r):
    combination = np.math.factorial(n)/(np.math.factorial(r)*np.math.factorial(n-r))# Equation: n!/(r!*(n-r)!)
    return combination

def partFour():

    N = 1000000
    hits = 0

    for j in range(N):
        hand = []
        deck = []
        # creates a deck
        for i in range(52):
            deck.append(i + 1)
        # choosing 6 cards
        while (len(hand) < 6):
            card = random.randint(1, 52)
            # if the card has been chosen,
            # chooses another card
            # if not, adds to hand
            if (deck.__contains__(card)):
                hand.append(card)
                deck.remove(card)

        # converting numbers to corresponding cards
        for i in range(6):
            hand[i] = hand[i] % 13

        # counting number of four of kinds
        for i in hand:
            if (hand.count(i) == 4):
                hits += 1
                break
                
    print("There were ", hits, " four of a kind in 100000 trials")
    print("After 1000000 tries the probability of '4 of a kind' in a 6-card poker draw is", hits / N)

    hands = C(52,6)
    rank = C(13,1)
    cards = C(4,4)
    remainder = C(48,2)

    result = (rank*cards*remainder)/hands

    print("The numerical probability of '4 of a kind' in a 6-card poker draw is: {:.10f}".format(result))

############ Main ####################################################################################

def main():
    keep_going = True
    while keep_going:
        print("Menu")
        print("1. Problem 1")
        print("2. Problem 2")
        print("3. Problem 3")
        print("4. Problem 4")
        print("5. Exit")

        user = int(input("Enter a number: "))
        if(user == 1):
            print("Running Problem 1...")
            partOne()
        if(user == 2):
            print("Running Problem 2...")
            partTwo()
        if(user == 3):
            print("Running Problem 3...")
            partThree()
        if(user == 4):
            print("Running Problem 4...")
            partFour()
        if(user == 5):
            print("Good bye...")
            keep_going = False

main()
        
