import matplotlib
import matplotlib.pyplot as plt
import numpy as np 
import random
import math
from math import sqrt
from numpy import sqrt
from numpy import e
from numpy import pi
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
from scipy.stats import norm
import scipy.integrate as integrate

def qOne():
    def pdf(x,mean,var):

        result = (1 / sqrt(2 * pi * var)) * (e ** ((-(x-mean)**2)/ (2*var)))
        return result

    def cdf(x, mean, var):


        result = (1/2) * (math.erf((x-mean)/(sqrt(2*var)))) + (1/2)
        return result


    x = np.arange(-6,7,.001)
    pairs = [(0,1),(0,10**-1),(0,10**-2),(-3,1),(-3,10**-1),(-3,10**-2)]
    allpdfResults = []
    allcdfResults = []



    for i in pairs:
        count = 0
        pdfResults = []
        for j in x:
            res = pdf(j,i[0],i[1])
            pdfResults.append(res)

        allpdfResults.append(pdfResults)

        plt3.plot(pdfResults)


    plt3.title('PDF')
    plt3.legend(['(0, 1)','(0, .1)','(0, .01)','(-3, 1)','(-3, .1)','(-3, .01)'],loc = "center right")
    plt3.show()


    for i in pairs:
        cdfResults = []
        for j in x:
            res = cdf(j,i[0],i[1])
            cdfResults.append(res)
        allcdfResults.append(cdfResults)
        plt4.plot(cdfResults)

    plt4.title('CDF')
    plt4.legend(['(0, 1)','(0, .1)','(0, .01)','(-3, 1)','(-3, .1)','(-3, .01)'],loc = "center right")
    plt4.show()

def qTwo():
    def method(n):
        #Generate the values of the RV X
        N = 100000; nbooks = n; a = 1; b = 3;
        mu_x = (a+b)/2 ; sig_x = np.sqrt((b-a)**2/12)
        print('Mean:',mu_x*n)
        print('Sig:',sig_x*np.sqrt(n))
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
    method(1)
    method(5)
    method(15)

def qThree():
    N = 100000
    nbattery = 24
    B = 45 #days
    mT = nbattery * B
    std_dev = B * sqrt(nbattery)
    X = np.zeros((N,1))
    for i in range(0,N):
        x = np.random.exponential(B,nbattery)
        w = np.sum(x)
        X[i] = w
    #nbins = 30
    edgecolor = 'w'
    bins = [float(x) for x in np.linspace(200,2000, 31)]
    h1,bin_edges = np.histogram(X,bins = bins, density = True)
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

    def gaussian(mu, sig,z):
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
        print("3. Problem 3")
        print("4. Exit")

        user = int(input("Enter a number: "))
        if(user == 1):
            print("Running Problem 1...")
            qOne()
        if(user == 2):
            print("Running Problem 2...")
            qTwo()
        if(user == 3):
            print("Running Problem 3...")
            qThree()
        if(user == 4):
            print("Good bye...")
            keep_going = False

main()
