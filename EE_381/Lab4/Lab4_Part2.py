import numpy as np
import matplotlib
import matplotlib.pyplot as plt

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