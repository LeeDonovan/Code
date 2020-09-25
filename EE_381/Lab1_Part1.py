import numpy as np
import matplotlib.pyplot as plt
import random

N=100000
max_rolls = 60
results = np.zeros(N, 1)
for i in range(N):
    d1=np.zeros(max_rolls, 1)
    d2=np.zeros(max_rolls, 1)
    
    for j in range(max_rolls):
        d1[j, :] = random.randint(1,6)
        d2[j, :] = random.randint(1,6)
    sum = d1 + d2
    counter = 0
    while counter < len(sum):
        if sum[counter][0] == 7:
            results[i] = counter
            break
        counter+=1
b = range(0,60)
sb = np.size(b)
h1, binedges = np.histogram(results, bins = b)
b1 = binedges[0:sb-1]

fig1=plt.figure(1)
plt.stem(b1,h1)
plt.title('Stem plot - Number Of Rolls for a Sum Of 7')
plt.xlabel('Number Of Rolls')
plt.ylabel('Number of occurrences')
fig1.savefig('Sum of Two Dices Equal to Seven.jpg')

fig2=plt.figure(2)
p1=h1/N
print(p1[0])
print(p1[1])
plt.stem(b1,p1)
plt.title('Stem plot - Number Of Rolls for a Sum Of 7: Probability mass function')
plt.xlabel('Number Of Rolls')
plt.ylabel('Number of occurrences')
fig2.savefig('PMF of Sum Of 7.jpg')