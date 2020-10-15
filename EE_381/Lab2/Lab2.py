import random

################### Part 1 #########################################################
def partOne():
    people = []
    trials = 10000000
    numOfA = 0
    numOfB = 0
    numOfC = 0
    A = 500
    B = 300
    C = 200
    for i in range(A):#adds letters A, B, and C into an array with their respective amount
        people.append('A')
    for i in range(B):
        people.append('B')
    for i in range(C):
        people.append('C')
    random.shuffle(people) #shuffles the array
    for i in range(trials):
        group = random.sample(people, 4)#Grabs 4 letters from the array 
        if all(person == 'A' for person in group):#checks to see if the group contains the same letter. 
            numOfA += 1
        elif all(person == 'B' for person in group):
            numOfB += 1
        elif all(person == 'C' for person in group):
            numOfC += 1
    print("Number of groups that are all A: ", numOfA)
    print("Number of groups that are all B: ", numOfB)
    print("Number of groups that are all C: ", numOfC)
    print("Probability of A is", numOfA/trials)
    print("Probability of B is", numOfB/trials)
    print("Probability of C is", numOfC/trials)

########################### Part 2 ##########################################################

def partTwo():
    kids = []
    trials = 100000
    same = 0
    n = int(input("Choose an n: (10 or 50)"))
    boys = 2*n
    girls = 2*n
    for i in range(boys):#adds letters B and G into an array
        kids.append('B')
    for i in range(girls):
        kids.append('G')
    random.shuffle(kids)#shuffles the array
    for i in range(trials):#runs 100000 times with 100000 different groups
        group = random.sample(kids,2*n)#chooses 2*n randomly from the array where n is a number the user inputted
        if  group.count('B') == group.count('G'):#checks to see if there's an even amount of boys and girls
            same += 1
    print("In",trials,"trials, the number of groups that contain an equal number of boys and girls:", same)
    print("Probability:", same/trials)

########################## Part 3 ##########################################################################

def partThree():
    trials = 1000000
    wins = 0
    print("Pick 4 different numbers, 1 through 20")
    picks = []
    numbers = []

    for i in range(20):#creates an array on 1-20
        numbers.append(i+1)
    print(numbers)

    for i in range(4):
        num = int(input())#user chooses 4 different numbers 
        picks.append(num)

    for i in range(trials):#runs the trial 1000000 times 
        lottery = random.sample(numbers,4)#lottery will hold 4 different numbers chosen randomly from numbers array
        if (set(lottery) == set(picks)):#checks to see if lottery numbers is the same as user's numbers
            wins += 1

    print(wins)
    print("Out of",trials,"trials, there were",wins,"wins")
    print("Probability:", wins/trials)

######################## Main ##################################################

def main():
    keep_going = True
    while keep_going:
        print("Menu")
        print("1. Problem 1")
        print("2. Problem 2")
        print("3. Problem 3")
        print("4. Exit")

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
            print("Good bye...")
            keep_going = False

main()