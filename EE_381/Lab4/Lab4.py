import matplotlib
import matplotlib.pyplot as plt
import numpy as np 
import random
import math
from math import sqrt

def qOne():
    print("WIP")

def qTwo():
    n = [1,5,10,15]
    #Generate the values of the RV X
    N = 100000; nbooks = 15; a = 1; b = 3;
    mu_x = (a+b)/2 ; sig_x = np.sqrt((b-a)**2/12)
    X = np.zeros((N,1))
    for k in range(0,N):
        x = np.random.uniform(a,b,nbooks)
        w = np.sum(x)
        X[k] = w
    #Create bins and histogram
    nbins = 30; #number of bins
    edgecolor = 'w' #Color separating bars in the bargraph
    bins = [float(x) for x in np.linspace(nbooks*a, nbooks*b, nbins+1)]
    h1, bin_edges = np.histogram(X,bins,density=True)
    # Define points on the horizontal xis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0] #Width of bars in the bargraph
    plt.close('all')
    #PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1,h1,width=barwidth, edgecolor=edgecolor)
    #Plot the gaussian function
    def gaussian(mu,sig,z):
        f = np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
        return f
    f = gaussian(mu_x*nbooks,sig_x*np.sqrt(nbooks),b1)
    plt.plot(b1,f,'r')
    plt.title('PDF Curve of Book Height with Gaussian')
    plt.show()

def qThree():
    N = 100000 #trial runs
    nbattery = 24#num batteries
    B = 45 #days
    mT = nbattery * B
    std_dev = B * sqrt(nbattery)
    X = np.zeros((N,1))#array of zeroes
    for i in range(0,N):
        x = np.random.exponential(B,nbattery)#create sample numbers 
        w = np.sum(x)
        X[i] = w
    edgecolor = 'w'
    bins = [float(x) for x in np.linspace(200,2000, 31)]
    h1,bin_edges = np.histogram(X,bins = bins, density = True)#create histogram
    be1 = bin_edges[0:np.size(bin_edges) - 1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1 + be2)/2
    barwidth = b1[1] - b1[0]
    plt.close('all')
    fig1 = plt.figure(1)
    plt.bar(b1,h1,width = barwidth, edgecolor = edgecolor)
    plt.title("PDF of Battey Carton Lifetime and Comparison with Gaussian")
    plt.xlabel("Battery Carton LIfetime")
    plt.ylabel("PDF")

    def gaussian(mu, sig,z):#create curve 
        f = np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
        return f

    f = gaussian(mT, std_dev,b1)
    plt.plot(b1,f,'r')
    plt.title('CDF of Battery Carton Lifetime')
    plt.xlabel("Battery Carton LIfetime for n = 24")
    plt.ylabel("CDF")
    plt.show()

def main():
    keep_going = True
    while keep_going:
        print("Menu")
        print("1. Problem 1")
        print("2. Problem 2")
        print("3. Problem 2")
        print("4. Exit")

        user = int(input("Enter a number: "))
        if(user == 1):
            print("Running Problem 1...")
            qOne()
        if(user == 2):
            print("Running Problem 2...")
            qTwo()
        if(user == 3):
            print("Running Problem 2...")
            qThree()
        if(user == 4):
            print("Good bye...")
            keep_going = False

main()
