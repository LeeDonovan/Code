import numpy as np
import random
from random import randint
import math
import matplotlib
import matplotlib.pyplot as plt
from numpy import histogram


def partOne():
    N = 1000000
    mean = 100
    std = 12
    sample_size = 200
    results = []
    for i in range(sample_size + 1):
        if (i == 0):#start at 1 so the incrementing makes sense from 1- 200 instead of 0-199
            i += 1
        sample_Data = []
        sample_Data.append(i)
        sum_x = 0
        N_x = np.random.normal(mean, std, i)
        for sample in range(len(N_x)):
            sum_x += N_x[sample]

        sample_std = std / math.sqrt(i)#get sample std

        # 95% confidence intervals
        lower_95 = mean - (1.96 * sample_std)
        upper_95 = mean + (1.96 * sample_std)
        # 99% confidence interval
        lower_99 = mean - (2.58 * sample_std)
        upper_99 = mean + (2.58 * sample_std)

        sample_Data.append(sum_x / i)#get the mean
        sample_Data.append(lower_95)
        sample_Data.append(upper_95)
        sample_Data.append(lower_99)
        sample_Data.append(upper_99)
        results.append(sample_Data)# add sample data into list to so it would be a tuple

    # Plot for 95%
    fig1 = plt.figure(1)
    plt.title("Sample Means of 95% Confidence Interval")
    plt.xlabel("Sample Size")
    plt.ylabel("mean")

    for i in range(sample_size):
        nx_sample = results[i][0]#grabs the sample
        nx_bar = results[i][1]#grabs the mean
        low_bound = results[i][2]#grabs the lower bound
        up_bound = results[i][3]#grabs upper bound

        plt.plot(nx_sample, nx_bar, 'xb')#plot the population
        plt.plot(nx_sample, up_bound, '.r')#creates the upper curve graph as color red
        plt.plot(nx_sample, low_bound, '.r')#creates the lower curve
    plt.show()
    # Plot for 99%
    fig2 = plt.figure(2)
    plt.title("Sample Means of 99% Confidence Interval")
    plt.xlabel("Sample Size")
    plt.ylabel("mean")

    for i in range(sample_size):
        nx_sample = results[i][0]#same as above but for the 99% confidence interval
        nx_bar = results[i][1]
        low_bound = results[i][2]
        up_bound = results[i][3]

        plt.plot(nx_sample, nx_bar, 'xb')
        plt.plot(nx_sample, up_bound, '.g')#color green 
        plt.plot(nx_sample, low_bound, '.g')
    plt.show()


def partTwoCalc(n, d, confidence, mean, std):
    s = 0
    zscore = [1.96, 2.58]
    fivevt = [2.776, 4.604]
    fourtyvt = [2.0227, 2.7079]
    onetwentyvt = [1.9801, 2.6178]
    val = np.random.normal(mean, std, n)
    sum_x = np.sum(val)
    bar_x = sum_x / n
    for i in range(len(val)):
        s += (val[i] - bar_x) ** 2
    s_hat = math.sqrt(s/(n-1))
    if (d == 0):
        if (confidence == 95):
            mean_upper = bar_x + zscore[0] * (s_hat/math.sqrt(n))
            mean_lower = bar_x - zscore[0] * (s_hat/math.sqrt(n))
        if (confidence == 99):
            mean_upper = bar_x + zscore[1] * (s_hat / math.sqrt(n))
            mean_lower = bar_x - zscore[1] * (s_hat / math.sqrt(n))
    if (d == 1):
        if(n == 5):
            if (confidence == 95):
                mean_upper = bar_x + fivevt[0] * (s_hat/math.sqrt(n))
                mean_lower = bar_x - fivevt[0] * (s_hat / math.sqrt(n))
            if (confidence == 99):
                mean_upper = bar_x + fivevt[1] * (s_hat/math.sqrt(n))
                mean_lower = bar_x - fivevt[1] * (s_hat / math.sqrt(n))
        if (n == 40):
            if (confidence == 95):
                mean_upper = bar_x + fourtyvt[0] * (s_hat / math.sqrt(n))
                mean_lower = bar_x - fourtyvt[0] * (s_hat / math.sqrt(n))
            if (confidence == 99):
                mean_upper = bar_x + fourtyvt[1] * (s_hat / math.sqrt(n))
                mean_lower = bar_x - fourtyvt[1] * (s_hat / math.sqrt(n))
        if (n == 120):
            if (confidence == 95):
                mean_upper = bar_x + onetwentyvt[0] * (s_hat / math.sqrt(n))
                mean_lower = bar_x - onetwentyvt[0] * (s_hat / math.sqrt(n))
            if (confidence == 99):
                mean_upper = bar_x + onetwentyvt[1] * (s_hat / math.sqrt(n))
                mean_lower = bar_x - onetwentyvt[1] * (s_hat / math.sqrt(n))
    if(mean_lower<mean<mean_upper):
        return 1
    else:
        return 0

def partTwo():
    N = 10000
    n = [5,40,120]
    nd, td = 0, 1
    mean = 100
    std = 12

    #n=5
    counter = 0
    for i in range(N):
        counter += partTwoCalc(n[0], nd, 95, mean, std)
    print("Probability of a 95% Confidence Interval for Normal Distribution of n = 5: ", counter / N)
    counter = 0
    for i in range(N):
        counter += partTwoCalc(n[0], nd, 99, mean, std)
    print("Probability of a 99% Confidence Interval for Normal Distribution of n = 5: ", counter / N)
    counter = 0
    for i in range(N):
        counter += partTwoCalc(n[0], td, 95, mean, std)
    print("Probability of a 95% Confidence Interval for Student's t Distribution of n = 5: ", counter / N)
    counter = 0
    for i in range(N):
        counter += partTwoCalc(n[0], td, 99, mean, std)
    print("Probability of a 99% Confidence Interval for Student's t Distribution of n = 5: ", counter / N)

    #n=40
    counter = 0
    for i in range(N):
        counter += partTwoCalc(n[1], nd, 95, mean, std)
    print("Probability of a 95% Confidence Interval for Normal Distribution of n = 40: ", counter / N)
    counter = 0
    for i in range(N):
        counter += partTwoCalc(n[1], nd, 99, mean, std)
    print("Probability of a 99% Confidence Interval for Normal Distribution of n = 40: ", counter / N)
    counter = 0
    for i in range(N):
        counter += partTwoCalc(n[1], td, 95, mean, std)
    print("Probability of a 95% Confidence Interval for Student's t Distribution of n = 40: ", counter / N)
    counter = 0
    for i in range(N):
        counter += partTwoCalc(n[1], td, 99, mean, std)
    print("Probability of a 99% Confidence Interval for Student's t Distribution of n = 40: ", counter / N)

    #n=120
    counter = 0
    for i in range(N):
        counter += partTwoCalc(n[2], nd, 95, mean, std)
    print("Probability of a 95% Confidence Interval for Normal Distribution of n = 120: ", counter / N)
    counter = 0
    for i in range(N):
        counter += partTwoCalc(n[2], nd, 99, mean, std)
    print("Probability of a 99% Confidence Interval for Normal Distribution of n = 120: ", counter / N)
    counter = 0
    for i in range(N):
        counter += partTwoCalc(n[2], td, 95, mean, std)
    print("Probability of a 95% Confidence Interval for Student's t Distribution of n = 120: ", counter / N)
    counter = 0
    for i in range(N):
        counter += partTwoCalc(n[2], td, 99, mean, std)
    print("Probability of a 99% Confidence Interval for Student's t Distribution of n = 120: ", counter / N)





def main():
    
    partOne()
    partTwo()

main()







