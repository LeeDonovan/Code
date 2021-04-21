import random
import numpy as np
import math

num_city = 100
num_air = 3
num_center = 5
sigma = 0.1
cities = set()
airports = []

for i in range(num_center):
    x = random.random()
    y = random.random()
    xc = np.random.normal(x, sigma, num_city//num_center)
    yc = np.random.normal(y, sigma, num_city//num_center)
    cities = cities.union(zip(xc, yc))


for i in range(num_air):
    x = random.random()
    y = random.random()
    airports.append((x,y)) 

import matplotlib.pyplot as plt

zip_cities = zip(*cities)
plt.scatter(*zip_cities, marker='+',color='b', label='Cities')
zip_airs = zip(*airports)
plt.scatter(*zip_airs, marker='*', color='r', s=100, label='Airports')
plt.legend()
plt.show()

d1 = []
d2 = []
d3 = []

for i in cities:
  shortest = 100000
  for j in range(len(airports)):
    d = math.sqrt((i[0] - airports[j][0])**2 + (i[1] - airports[j][1])**2)  
    if d < shortest:
      shortest = d
      airport = j
  if airport == 0:
    d1.append(i)
  elif airport == 1:
    d2.append(i)
  elif airport == 2:
    d3.append(i)



## objective function
s1 = 0
s2 = 0
s3 = 0
for i in d1:
  s1+= (airports[0][0]-i[0])**2 + (airports[0][1]-i[1])**2
for i in d2:
  s2+= (airports[1][0]-i[0])**2 + (airports[1][1]-i[1])**2
for i in d3:
  s3+= (airports[2][0]-i[0])**2 + (airports[2][1]-i[1])**2
s = s1 + s2 + s3
  
objfun = []
#print("objective function:",s)

for i in range(100):
  
  
  d1 = []
  d2 = []
  d3 = []
  
  for i in cities:
    shortest = 100000
    for j in range(len(airports)):
      d = math.sqrt((i[0] - airports[j][0])**2 + (i[1] - airports[j][1])**2)  
      if d < shortest:
        shortest = d
        airport = j
    if airport == 0:
      d1.append(i)
    elif airport == 1:
      d2.append(i)
    elif airport == 2:
      d3.append(i)
  
  
  
  s1 = 0
  s2 = 0
  s3 = 0
  for i in d1:
    s1+= (airports[0][0]-i[0])**2 + (airports[0][1]-i[1])**2
  for i in d2:
    s2+= (airports[1][0]-i[0])**2 + (airports[1][1]-i[1])**2
  for i in d3:
    s3+= (airports[2][0]-i[0])**2 + (airports[2][1]-i[1])**2
  s = s1 + s2 + s3
  print("objective function:",s)
  objfun.append(s)

  dfx1 = 0
  dfx2 = 0
  dfx3 = 0
  dfy1 = 0
  dfy2 = 0
  dfy3 = 0


  for i in d1:
    dfx1+= airports[0][0] - i[0]
  for i in d2:
    dfx2+= airports[1][0] - i[0]
  for i in d3:
    dfx3+= airports[2][0] - i[0]
  for i in d1:
    dfy1+= airports[0][1] - i[1]
  for i in d2:
    dfy2+= airports[1][1] - i[1]
  for i in d3:
    dfy3+= airports[2][1] - i[1]
  dfx1 = dfx1 * 2
  dfx2 = dfx2 * 2
  dfx3 = dfx3 * 2
  dfy1 = dfy1 * 2
  dfy2 = dfy2 * 2
  dfy3 = dfy3 * 2

  #print("dfx1:",dfx1)
  for i in range(len(airports)):
    airports[i] = list(airports[i])

  a = .01

  airports[0][0]-= a*dfx1 
  airports[0][1]-= a*dfy1 
  airports[1][0]-= a*dfx2 
  airports[1][1]-= a*dfy2 
  airports[2][0]-= a*dfx3 
  airports[2][1]-= a*dfy3 
  #print("airport location:",airports)

import matplotlib.pyplot as plt1

zip_cities = zip(*cities)
plt1.scatter(*zip_cities, marker='+',color='b', label='Cities')
zip_airs = zip(*airports)
plt1.scatter(*zip_airs, marker='*', color='r', s=100, label='Airports')
plt1.legend()
plt1.show()
num_list = []
for i in range(len(objfun)):
  num_list.append(i)
import matplotlib.pyplot as plt2
#zip_objfun = zip(num_list, objfun)
plt2.scatter(num_list,objfun, marker='o',color='b', label='Objective Function')
plt2.show()