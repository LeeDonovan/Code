import matplotlib
import matplotlib.pyplot as plt
import numpy as np 
import random
import math
from math import sqrt

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
