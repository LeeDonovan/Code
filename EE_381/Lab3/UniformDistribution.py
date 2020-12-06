import matplotlib.pyplot as plt
from matplotlib.pyplot import xticks
from scipy.stats import uniform
import numpy as np 
import random


def partOne():
    def genRandos(a, b, x):#rando func
        xValues = set()#set a sequence that can be converted to anything
        while x != len(xValues):
            rando = random.uniform(a,b)#get rando nums
            xValues.add(rando)
        return xValues#return list of rando nums

    def pdf(x_Values, N):#first part for pdf list
        a , b= (1,10)
        f_x = 1/(b-a)#formula
        pdf_list = []
        for i in x_Values:#test rando numbers against increment
            if(i <= a or i >= b):#test to make sure a isn't negative or greater than b to get 0
                pdf_list.append(0)
            else:
                pdf_list.append(f_x)
        return pdf_list#return list when finished

    def cdf(x_Values, N):
        a , b= (1,10)
        cdf_list = []
        for i in x_Values:#test rando nums against increment 
            f_x = (i - a) / (b-a)#function is used every round if needed
            if(i <= a):#test if negative
                cdf_list.append(0)
            elif(i >= b):#greater than 10
                cdf_list.append(1)
            else:
                cdf_list.append(f_x)#if none of the conditions happened then we grab the function
        return cdf_list

    def run():
        N = 10000#experiments
        x_Values = sorted(genRandos(0,11,N))#get rando nums
        pdf_list = pdf(x_Values,N)#list returned
        cdf_list = cdf(x_Values,N)
        
        fig, axs = plt.subplots(2)#created 2 graphs
        fig.suptitle("Part A")
        plt.setp(axs, xticks  =[0,1,2,3,4,5,6,7,8,9,10,11])#x marks
        axs[0].plot(list(x_Values), pdf_list)#sorted values with appended pdf list
        axs[0].set_title("Probability Distribution Function")
        axs[1].plot(list(x_Values), cdf_list)#sorted values with appended cdf list
        axs[1].set_title("Cumulative Distribution Function")

        #Using stats.uniform for pdf and cdf
        x = np.linspace(0,11,10000)#spacing for graph points
        fig, axs = plt.subplots(2)
        fig.suptitle("Part B")
        plt.setp(axs, xticks  =[0,1,2,3,4,5,6,7,8,9,10,11])
        axs[0].plot(x, uniform.pdf(x , 1, 9))#pre built function for pdf
        axs[0].set_title("Probability Distribution Function")
        axs[1].plot(x, uniform.cdf(x, 1, 9))#prebuilt function for cdf
        axs[1].set_title("Cumulative Distribution Function")
        plt.show()  
    run()

def partTwo():
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

        