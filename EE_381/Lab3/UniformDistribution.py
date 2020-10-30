import numpy as np
import matplotlib.pyplot as plt

def partOne():
    n = 100000
    counter = 0
    points = 3
    pie = 2*np.pi
    half = 180
    checker = 0

    np.random.seed()
    inside = False
    for i in range(n):
        opposites = []
        theta = np.random.uniform(0,360,3)
        radius = 3
        
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        holder = 0
        for j in range(3):
            holder = x[j]
        for i in theta:
            if(i > 180):
                opposite = i - 180
                opposites.append(opposite)
            else:
                opposite = i + 180
                opposites.append(opposite)

        for i in range(3):
            if(i == 0):
                if (theta[i] > opposites[i]):
                    if ((opposites[i] < theta[1] < theta[i]) and opposites[i] < theta[2] < theta[i]):
                        inside = True
                    elif (not(opposites[i] < theta[1] < theta[i]) and not(opposites[i] < theta[2] < theta[i])):
                        inside = True
                elif((theta[i] < theta[1] < opposites[i]) and theta[i] < theta[2] < opposites[i]):
                    inside = True
                elif(not(theta[i] < theta[1] < opposites[i]) and not(theta[i] < theta[2] < opposites[i])):
                    inside = True
            if (i == 1):
                if (theta[i] > opposites[i]):
                    if ((opposites[i] < theta[0] < theta[i]) and opposites[i] < theta[2] < theta[i]):
                        inside = True
                    elif (not (opposites[i] < theta[0] < theta[i]) and not (opposites[i] < theta[2] < theta[i])):
                        inside = True
                elif ((theta[i] < theta[0] < opposites[i]) and theta[i] < theta[2] < opposites[i]):

                    inside = True
                elif (not (theta[i] < theta[0] < opposites[i]) and not (theta[i] < theta[2] < opposites[i])):
                    inside = True
            if (i == 2):
                if (theta[i] > opposites[i]):
                    if ((opposites[i] < theta[1] < theta[i]) and opposites[i] < theta[0] < theta[i]):
                        inside = True
                    elif (not (opposites[i] < theta[1] < theta[i]) and not (opposites[i] < theta[0] < theta[i])):
                        inside = True
                elif ((theta[i] < theta[1] < opposites[i]) and theta[i] < theta[0] < opposites[i]):
                    inside = True
                elif (not (theta[i] < theta[1] < opposites[i]) and not (theta[i] < theta[0] < opposites[i])):
                    inside = True
        if(inside):
            counter+=1
        inside = False
    print("Out of ", n, "tries, ", counter," had 3 points that were within a semi circle giving us the probability of ", counter/n, "%")


def main():
    keep_going = True
    while keep_going:
        print("Menu")
        print("1. Problem 1")
        print("2. Problem 2")
        print("3. Exit")

        user = int(input("Enter a number: "))
        if(user == 1):
            print("Running Problem 1...")
            partOne()
        if(user == 2):
            print("Running Problem 2...")
            partTwo()
        if(user == 3):
            print("Good bye...")
            keep_going = False

main()

        