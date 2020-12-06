import matplotlib.pyplot as plt
from matplotlib.pyplot import x_axis 
from scipy.stats import uniform
import numpy as np 
import random


def genRandos(a, b, x):
    xValues = set()
    while x != len(xValues):
        rando = random.uniform(a,b)
        xValues.add(rando)
    return xValues

def pdf(x_Values, N):
    a , b= (1,10)
    f_x = 1/(b-a)#formula
    pdf_list = []
    x_Values = sorted(genRandos(0,11,N))
    for i in x_Values:
        if(i <= a or i >= b):
            pdf_list.append(0)
        else:
            pdf_list.append(f_x)
    return pdf_list

def cdf(x_Values, N):
    a , b= (1,10)
    cdf_list = []
    for i in x_Values:
        f_x = (i - a) / (b-a)
        if(i <= a):
            cdf_list.append(0)
        elif(i >= b):
            cdf_list.append(1)
        else:
            cdf_list.append(f_x)
    return cdf_list

def PDF_CDF():
    N = 10000
    x_Values = sorted(genRandos(0,11,N))
    pdf_list = pdf(x_Values,N)
    cdf_list = cdf(x_Values,N)
    
    fig, axs = plt.subplots(2)
    fig.suptitle("Part A")
    plt.setp(axs, x_axis  =[0,1,2,3,4,5,6,7,8,9,10,11])
    axs[0].plot(list(x_Values), pdf_list)#sorted values with appended list
    axs[0].set_title("Probability Distribution Function")
    axs[1].plot(list(x_Values), cdf_list)
    axs[1].set_title("Cumulative Distribution Function")

    #Using stats.uniform for pdf and cdf
    x = np.linspace(0,11,10000)
    fig, axs = plt.subplots(2)
    fig.suptitle("Part B")
    plt.setp(axs, x_axis  =[0,1,2,3,4,5,6,7,8,9,10,11])
    axs[0].plot(x, uniform.pdf(x , 1, 9))
    axs[0].set_title("Probability Distribution Function")
    axs[1].plot(x, uniform.cdf(x, 1, 9))
    axs[1].set_title("Cumulative Distribution Function")
    plt.show()  