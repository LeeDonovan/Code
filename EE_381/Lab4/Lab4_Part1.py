import math
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
def pdf(x,mean,var):

    result = (1 / sqrt(2 * pi * var)) * (e ** ((-(x-mean)**2)/ (2*var)))
    return result

def cdf(x, mean, var):

    #result = (math.erf(((sqrt(2)*x) - (sqrt(2)*mean))/(2*sqrt(var))) + 1)/2
    result = (1/2) * (math.erf((x-mean)/(sqrt(2*var)))) + (1/2)
    return result

#x = range(-6,7)
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
    #res = pdf(i,pairs[0][0],pairs[0][1])
    #print(pdfResults)
    allpdfResults.append(pdfResults)

    plt3.plot(pdfResults)

    #print(res)
#print(allpdfResults)
plt3.title('PDF')
plt3.legend(['(0, 1)','(0, .1)','(0, .01)','(-3, 1)','(-3, .1)','(-3, .01)'],loc = "center right")
plt3.show()

#for i in allpdfResults:
#   plt1.stem(range(-6,7),i)

#plt.stem(range(-6,7),pdfResults)
#plt.stem(range(0,13),pdfResults)
#plt1.title("PDF")
#plt1.show()

for i in pairs:
    cdfResults = []
    for j in x:
        res = cdf(j,i[0],i[1])
        cdfResults.append(res)
    #res = pdf(i,pairs[0][0],pairs[0][1])
    #print(cdfResults)
    allcdfResults.append(cdfResults)
    plt4.plot(cdfResults)
    #print(res)
#print(allpdfResults)
plt4.title('CDF')
plt4.legend(['(0, 1)','(0, .1)','(0, .01)','(-3, 1)','(-3, .1)','(-3, .01)'],loc = "center right")
plt4.show()
#for i in allcdfResults:
#    plt2.stem(range(-6,7),i)

#plt.stem(range(-6,7),pdfResults)
#plt.stem(range(0,13),pdfResults)
#plt2.title("CDF")
#plt2.show()
