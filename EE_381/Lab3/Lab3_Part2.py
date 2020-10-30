import numpy as np
import matplotlib.pyplot as plt

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
    radius = 3#np.random.uniform(0, 5, points) ** 0.5
    
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
                    #print("inside")
                    #counter+=1
                    inside = True
                elif (not(opposites[i] < theta[1] < theta[i]) and not(opposites[i] < theta[2] < theta[i])):
                    #print("not inside")
                    #counter += 1
                    inside = True
            elif((theta[i] < theta[1] < opposites[i]) and theta[i] < theta[2] < opposites[i]):
                #print("inside")
                #counter += 1
                inside = True
            elif(not(theta[i] < theta[1] < opposites[i]) and not(theta[i] < theta[2] < opposites[i])):
                #print("not inside")
                #counter += 1
                inside = True
        if (i == 1):
            if (theta[i] > opposites[i]):
                if ((opposites[i] < theta[0] < theta[i]) and opposites[i] < theta[2] < theta[i]):
                    #print("inside")
                    #counter += 1
                    inside = True
                elif (not (opposites[i] < theta[0] < theta[i]) and not (opposites[i] < theta[2] < theta[i])):
                    #print("not inside")
                    #counter += 1
                    inside = True
            elif ((theta[i] < theta[0] < opposites[i]) and theta[i] < theta[2] < opposites[i]):
                #print("inside")
                #counter += 1
                inside = True
            elif (not (theta[i] < theta[0] < opposites[i]) and not (theta[i] < theta[2] < opposites[i])):
                #print("not inside")
                #counter += 1
                inside = True
        if (i == 2):
            if (theta[i] > opposites[i]):
                if ((opposites[i] < theta[1] < theta[i]) and opposites[i] < theta[0] < theta[i]):
                    #print("inside")
                    #counter += 1
                    inside = True
                elif (not (opposites[i] < theta[1] < theta[i]) and not (opposites[i] < theta[0] < theta[i])):
                    #print("not inside")
                    #counter += 1
                    inside = True
            elif ((theta[i] < theta[1] < opposites[i]) and theta[i] < theta[0] < opposites[i]):
                #print("inside")
                #counter += 1
                inside = True
            elif (not (theta[i] < theta[1] < opposites[i]) and not (theta[i] < theta[0] < opposites[i])):
                #print("not inside")
                #counter += 1
                inside = True
    if(inside):
        counter+=1
    inside = False
print("Out of ", n, "tries, ", counter," had 3 points that were within a semi circle giving us the probability of ", counter/n, "%")

        